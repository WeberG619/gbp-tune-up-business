#!/usr/bin/env python3
"""
Local Market Mapper - Find and map poorly-optimized businesses in your area

Creates:
1. CSV with all businesses and scores
2. Google Maps KML file (open in Google Maps)
3. Interactive HTML map
4. Prioritized target list

Usage:
    python tools/market_mapper.py --locations "Sandpoint, ID" "Coeur d'Alene, ID" "Spokane, WA"
    python tools/market_mapper.py --demo  # Test with demo data
"""

import os
import sys
import csv
import argparse
from datetime import datetime
from pathlib import Path
import json

# Try to import from lead_finder
try:
    from lead_finder import LeadFinder, GBPAuditor
except:
    sys.path.insert(0, os.path.dirname(__file__))
    from lead_finder import LeadFinder


def generate_kml(leads, output_file):
    """Generate KML file for Google Maps/Earth"""

    kml = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.org/kml/2.2">
<Document>
    <name>GBP Optimization Targets</name>
    <description>Local businesses that need Google Business Profile optimization</description>

    <Style id="high_priority">
        <IconStyle>
            <color>ff0000ff</color>
            <scale>1.2</scale>
            <Icon>
                <href>http://maps.google.com/mapfiles/kml/paddle/red-stars.png</href>
            </Icon>
        </IconStyle>
    </Style>

    <Style id="medium_priority">
        <IconStyle>
            <color>ff00ffff</color>
            <scale>1.0</scale>
            <Icon>
                <href>http://maps.google.com/mapfiles/kml/paddle/ylw-stars.png</href>
            </Icon>
        </IconStyle>
    </Style>

    <Style id="low_priority">
        <IconStyle>
            <color>ff00ff00</color>
            <scale>0.8</scale>
            <Icon>
                <href>http://maps.google.com/mapfiles/kml/paddle/grn-circle.png</href>
            </Icon>
        </IconStyle>
    </Style>
"""

    for lead in leads:
        priority = lead.get('priority', 'MEDIUM').lower()
        style = f"{priority}_priority"

        # Create placemark description
        desc = f"""
Business: {lead.get('business_name', 'Unknown')}
Phone: {lead.get('phone', 'Not listed')}
Rating: {lead.get('rating', 'N/A')} stars
Reviews: {lead.get('reviews', 0)}
Photos: {lead.get('photos', 0)}

SCORE: {lead.get('score', 0)}/100
Priority: {lead.get('priority', 'MEDIUM')}

Issues:
{lead.get('reasons', 'No specific issues identified')}

Address: {lead.get('address', 'Address not available')}
"""

        # Note: We don't have actual coordinates without API, so we skip location
        # In real version with API, we'd add coordinates here
        kml += f"""
    <Placemark>
        <name>{lead.get('business_name', 'Unknown')}</name>
        <description><![CDATA[{desc}]]></description>
        <styleUrl>#{style}</styleUrl>
    </Placemark>
"""

    kml += """
</Document>
</kml>
"""

    with open(output_file, 'w') as f:
        f.write(kml)

    print(f"📍 KML file saved: {output_file}")
    print(f"   Open in Google Maps: https://www.google.com/maps/d/")
    print(f"   Click 'Create a new map' → Import → Upload {output_file}")


def generate_html_map(leads, output_file, locations):
    """Generate interactive HTML map"""

    # Group leads by location
    by_location = {}
    for lead in leads:
        loc = lead.get('location', 'Unknown')
        if loc not in by_location:
            by_location[loc] = []
        by_location[loc].append(lead)

    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>GBP Optimization Target Map</title>
    <meta charset="utf-8">
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f5f5f5;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
        }}
        .header h1 {{
            margin: 0 0 10px 0;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .stat-number {{
            font-size: 36px;
            font-weight: bold;
            color: #667eea;
        }}
        .stat-label {{
            color: #666;
            margin-top: 5px;
        }}
        .location-section {{
            background: white;
            padding: 25px;
            margin-bottom: 25px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .location-header {{
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
            color: #333;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }}
        .lead-grid {{
            display: grid;
            gap: 15px;
        }}
        .lead-card {{
            border: 2px solid #e0e0e0;
            padding: 20px;
            border-radius: 8px;
            transition: all 0.3s;
        }}
        .lead-card:hover {{
            border-color: #667eea;
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.2);
        }}
        .lead-card.high {{
            border-left: 5px solid #dc3545;
            background: #fff5f5;
        }}
        .lead-card.medium {{
            border-left: 5px solid #ffc107;
            background: #fffef5;
        }}
        .lead-card.low {{
            border-left: 5px solid #28a745;
            background: #f5fff5;
        }}
        .lead-header {{
            display: flex;
            justify-content: space-between;
            align-items: start;
            margin-bottom: 15px;
        }}
        .business-name {{
            font-size: 20px;
            font-weight: bold;
            color: #333;
        }}
        .score {{
            font-size: 24px;
            font-weight: bold;
            padding: 5px 15px;
            border-radius: 5px;
        }}
        .score.high {{
            background: #dc3545;
            color: white;
        }}
        .score.medium {{
            background: #ffc107;
            color: #333;
        }}
        .score.low {{
            background: #28a745;
            color: white;
        }}
        .lead-details {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 10px;
            margin: 15px 0;
            padding: 15px;
            background: white;
            border-radius: 5px;
        }}
        .detail {{
            text-align: center;
        }}
        .detail-label {{
            font-size: 12px;
            color: #666;
            text-transform: uppercase;
        }}
        .detail-value {{
            font-size: 18px;
            font-weight: bold;
            color: #333;
            margin-top: 5px;
        }}
        .issues {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            margin-top: 15px;
        }}
        .issues-title {{
            font-weight: bold;
            color: #666;
            margin-bottom: 10px;
        }}
        .contact-info {{
            margin-top: 15px;
            padding-top: 15px;
            border-top: 1px solid #e0e0e0;
            color: #666;
        }}
        .action-buttons {{
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }}
        .btn {{
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            text-decoration: none;
            display: inline-block;
            text-align: center;
        }}
        .btn-primary {{
            background: #667eea;
            color: white;
        }}
        .btn-secondary {{
            background: #e0e0e0;
            color: #333;
        }}
        .filter-bar {{
            background: white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .filter-buttons {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}
        .filter-btn {{
            padding: 10px 20px;
            border: 2px solid #e0e0e0;
            background: white;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
        }}
        .filter-btn.active {{
            background: #667eea;
            color: white;
            border-color: #667eea;
        }}
        .export-section {{
            background: white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🎯 Your GBP Optimization Target Market</h1>
        <p>Businesses in your area that need your service</p>
        <p><strong>Locations:</strong> {', '.join(locations)}</p>
    </div>

    <div class="stats">
        <div class="stat-card">
            <div class="stat-number">{len(leads)}</div>
            <div class="stat-label">Total Leads</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{sum(1 for l in leads if l.get('priority') == 'HIGH')}</div>
            <div class="stat-label">High Priority</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{sum(1 for l in leads if l.get('priority') == 'MEDIUM')}</div>
            <div class="stat-label">Medium Priority</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">${len(leads) * 179:,}</div>
            <div class="stat-label">Potential Revenue</div>
        </div>
    </div>

    <div class="export-section">
        <h3>📥 Export Your Data</h3>
        <p>All leads saved to CSV and KML files in the maps/ folder</p>
        <p>Open the KML file in Google Maps to see pins on actual map</p>
    </div>

    <div class="filter-bar">
        <strong>Filter by Priority:</strong>
        <div class="filter-buttons">
            <button class="filter-btn active" onclick="filterLeads('all')">All ({len(leads)})</button>
            <button class="filter-btn" onclick="filterLeads('high')">High Priority ({sum(1 for l in leads if l.get('priority') == 'HIGH')})</button>
            <button class="filter-btn" onclick="filterLeads('medium')">Medium Priority ({sum(1 for l in leads if l.get('priority') == 'MEDIUM')})</button>
        </div>
    </div>
"""

    # Generate sections for each location
    for location, location_leads in by_location.items():
        location_leads.sort(key=lambda x: x.get('score', 0), reverse=True)

        html += f"""
    <div class="location-section">
        <div class="location-header">
            📍 {location}
            <span style="font-size: 16px; color: #666; font-weight: normal;">
                ({len(location_leads)} businesses)
            </span>
        </div>
        <div class="lead-grid">
"""

        for lead in location_leads:
            priority_class = lead.get('priority', 'MEDIUM').lower()

            html += f"""
            <div class="lead-card {priority_class}" data-priority="{priority_class}">
                <div class="lead-header">
                    <div class="business-name">{lead.get('business_name', 'Unknown Business')}</div>
                    <div class="score {priority_class}">{lead.get('score', 0)}</div>
                </div>

                <div class="lead-details">
                    <div class="detail">
                        <div class="detail-label">Photos</div>
                        <div class="detail-value">{lead.get('photos', 0)}</div>
                    </div>
                    <div class="detail">
                        <div class="detail-label">Reviews</div>
                        <div class="detail-value">{lead.get('reviews', 0)}</div>
                    </div>
                    <div class="detail">
                        <div class="detail-label">Rating</div>
                        <div class="detail-value">{lead.get('rating', 'N/A')}★</div>
                    </div>
                    <div class="detail">
                        <div class="detail-label">Priority</div>
                        <div class="detail-value">{lead.get('priority', 'MEDIUM')}</div>
                    </div>
                </div>

                <div class="issues">
                    <div class="issues-title">🎯 Opportunities:</div>
                    {lead.get('reasons', 'Profile needs optimization')}
                </div>

                <div class="contact-info">
                    📍 {lead.get('address', 'Address not available')}<br>
                    📞 {lead.get('phone', 'Phone not listed')}<br>
                    🌐 {lead.get('website', 'No website')}
                </div>

                <div class="action-buttons">
                    <a href="tel:{lead.get('phone', '')}" class="btn btn-primary">📞 Call</a>
                    <button class="btn btn-secondary" onclick="copyInfo('{lead.get('business_name', '')}', '{lead.get('phone', '')}', '{lead.get('address', '')}')">📋 Copy Info</button>
                </div>
            </div>
"""

        html += """
        </div>
    </div>
"""

    html += """
    <script>
        function filterLeads(priority) {
            const cards = document.querySelectorAll('.lead-card');
            const buttons = document.querySelectorAll('.filter-btn');

            // Update button states
            buttons.forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');

            // Filter cards
            cards.forEach(card => {
                if (priority === 'all' || card.dataset.priority === priority) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        }

        function copyInfo(name, phone, address) {
            const text = `Business: ${name}\\nPhone: ${phone}\\nAddress: ${address}`;
            navigator.clipboard.writeText(text).then(() => {
                alert('✅ Contact info copied to clipboard!');
            });
        }
    </script>
</body>
</html>
"""

    with open(output_file, 'w') as f:
        f.write(html)

    print(f"🗺️  HTML map saved: {output_file}")
    print(f"   Open in browser to view interactive map")


def create_action_plan(leads, output_file):
    """Create a prioritized action plan"""

    # Sort by score (highest first = worst profiles = best opportunities)
    leads.sort(key=lambda x: x.get('score', 0), reverse=True)

    content = f"""# 🎯 YOUR ACTION PLAN - {len(leads)} Target Businesses

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}

---

## 📊 MARKET SUMMARY

**Total Businesses Found:** {len(leads)}
**High Priority:** {sum(1 for l in leads if l.get('priority') == 'HIGH')}
**Medium Priority:** {sum(1 for l in leads if l.get('priority') == 'MEDIUM')}
**Low Priority:** {sum(1 for l in leads if l.get('priority') == 'LOW')}

**Potential Revenue:** ${len(leads) * 179:,} (if you close all)
**Realistic Revenue (30% close rate):** ${int(len(leads) * 0.3 * 179):,}

---

## 🚀 THIS WEEK: TOP 10 TARGETS

Focus on these first - highest scores = biggest problems = easiest sells:

"""

    for i, lead in enumerate(leads[:10], 1):
        content += f"""
### {i}. {lead.get('business_name', 'Unknown')} (Score: {lead.get('score', 0)})

**Priority:** {lead.get('priority', 'MEDIUM')} 🔥
**Phone:** {lead.get('phone', 'Not listed')}
**Address:** {lead.get('address', 'Not available')}

**Why they need you:**
{lead.get('reasons', 'Profile needs optimization')}

**Your pitch:**
"Hi, I noticed {lead.get('business_name', 'your business')} only has {lead.get('photos', 3)} photos on Google
while competitors average 20+. This is probably costing you customers.
I can fix it in 90 minutes for $179. Can I show you a quick audit?"

**Status:** [ ] Called [ ] Emailed [ ] Visited [ ] Closed

---
"""

    content += f"""
## 📅 WEEK 2-4: NEXT {min(20, len(leads)-10)} TARGETS

"""

    for i, lead in enumerate(leads[10:30], 11):
        content += f"""{i}. **{lead.get('business_name', 'Unknown')}** (Score: {lead.get('score', 0)}) - {lead.get('phone', 'No phone')}
"""

    content += """

---

## 💡 OUTREACH STRATEGY

### Option 1: Walk-In (Best for first 5)
1. Print top 10 audit reports
2. Map route in Google Maps
3. Visit 8-10 businesses in one afternoon
4. Use pitch script from sales-materials/pitch_scripts.md
5. Expected: 1-2 clients

### Option 2: Phone Calls
1. Call top 20 from this list
2. Use phone script
3. Offer to email audit report
4. Follow up next day
5. Expected: 2-4 interested, 1 client

### Option 3: Email Outreach
1. Find emails (website, call and ask)
2. Send personalized email from templates
3. Attach their audit report
4. Follow up in 3 days
5. Expected: 3-5 responses, 1 client

---

## ✅ DAILY CHECKLIST

**Morning (30 min):**
- [ ] Review top 5 targets for today
- [ ] Plan route / gather phone numbers
- [ ] Print audit reports (if walk-in)

**Afternoon (2-3 hours):**
- [ ] Contact 8-10 businesses (walk/call/email)
- [ ] Track results in spreadsheet
- [ ] Follow up with interested leads

**Evening (30 min):**
- [ ] Update status for each contact
- [ ] Schedule service for closed clients
- [ ] Plan tomorrow's targets

---

## 📈 EXPECTED RESULTS

**Week 1:** 2-3 clients = $358-537
**Week 2:** 3-5 clients = $537-895
**Week 3:** 5-8 clients = $895-1,432
**Week 4:** 8-10 clients = $1,432-1,790

**Month 1 Total: $3,222-4,654**

---

## 🎯 SUCCESS METRICS

Track these weekly:
- Businesses contacted: ___
- Responses received: ___
- Meetings/demos: ___
- Clients closed: ___
- Revenue generated: $___

---

**Open the HTML map to see all businesses visually!**
**File: maps/market_map_[timestamp].html**
"""

    with open(output_file, 'w') as f:
        f.write(content)

    print(f"📋 Action plan saved: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description='Map your local market - find businesses that need your service'
    )
    parser.add_argument('--locations', nargs='+',
                       default=['Sandpoint, ID', 'Coeur d\'Alene, ID', 'Spokane, WA'],
                       help='Cities to search (e.g., "Austin, TX" "Dallas, TX")')
    parser.add_argument('--industries', nargs='+',
                       default=['coffee shop', 'salon', 'gym', 'restaurant'],
                       help='Industries to target')
    parser.add_argument('--limit', type=int, default=20,
                       help='Businesses per location/industry (default: 20)')
    parser.add_argument('--min-score', type=int, default=40,
                       help='Minimum lead quality score (default: 40)')
    parser.add_argument('--demo', action='store_true',
                       help='Use demo mode (no API required)')
    parser.add_argument('--api-key', help='Google Places API key')

    args = parser.parse_args()

    print("=" * 60)
    print("🗺️  LOCAL MARKET MAPPER")
    print("=" * 60)
    print(f"\nSearching in: {', '.join(args.locations)}")
    print(f"Industries: {', '.join(args.industries)}")
    print(f"Limit: {args.limit} per location/industry\n")

    # Initialize finder
    api_key = None if args.demo else args.api_key
    finder = LeadFinder(api_key=api_key)

    # Collect all leads
    all_leads = []

    for location in args.locations:
        for industry in args.industries:
            print(f"\n🔍 Searching: {industry} in {location}")

            leads = finder.find_leads(
                query=industry,
                location=location,
                limit=args.limit,
                min_score=args.min_score
            )

            # Add location info
            for lead in leads:
                lead['location'] = location
                lead['industry'] = industry

            all_leads.extend(leads)
            print(f"   Found: {len(leads)} qualified leads")

    if not all_leads:
        print("\n❌ No leads found. Try:")
        print("  - Lower --min-score threshold")
        print("  - Different industries")
        print("  - Use --demo mode to test")
        return

    # Create output directory
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = Path('maps')
    output_dir.mkdir(exist_ok=True)

    # Generate outputs
    print(f"\n{'=' * 60}")
    print("📊 GENERATING MARKET INTELLIGENCE")
    print('=' * 60)

    # 1. Save CSV
    csv_file = output_dir / f'market_leads_{timestamp}.csv'
    fieldnames = ['priority', 'score', 'business_name', 'industry', 'location',
                  'phone', 'address', 'rating', 'reviews', 'photos', 'website', 'reasons']

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(all_leads)

    print(f"\n✅ CSV saved: {csv_file}")

    # 2. Generate KML
    kml_file = output_dir / f'market_map_{timestamp}.kml'
    generate_kml(all_leads, kml_file)

    # 3. Generate HTML map
    html_file = output_dir / f'market_map_{timestamp}.html'
    generate_html_map(all_leads, html_file, args.locations)

    # 4. Generate action plan
    plan_file = output_dir / f'action_plan_{timestamp}.md'
    create_action_plan(all_leads, plan_file)

    # Summary
    print(f"\n{'=' * 60}")
    print("🎉 YOUR MARKET MAP IS READY!")
    print('=' * 60)
    print(f"\n📁 All files saved to: {output_dir}/")
    print(f"\n📊 MARKET SUMMARY:")
    print(f"   Total Businesses: {len(all_leads)}")
    print(f"   High Priority: {sum(1 for l in all_leads if l.get('priority') == 'HIGH')}")
    print(f"   Medium Priority: {sum(1 for l in all_leads if l.get('priority') == 'MEDIUM')}")
    print(f"   Potential Revenue: ${len(all_leads) * 179:,}")
    print(f"\n🎯 NEXT STEPS:")
    print(f"   1. Open HTML map: {html_file}")
    print(f"   2. Read action plan: {plan_file}")
    print(f"   3. Start with top 10 targets")
    print(f"   4. Track progress in CSV")
    print(f"\n💡 TIP: Import KML to Google Maps for turn-by-turn directions!")
    print()


if __name__ == '__main__':
    main()
