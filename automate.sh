#!/bin/bash

###############################################################################
# COMPLETE BUSINESS AUTOMATION
# Runs your entire GBP optimization business automatically
###############################################################################

echo "=========================================================================="
echo "🤖 COMPLETE BUSINESS AUTOMATION"
echo "=========================================================================="
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found! Please install Python 3."
    exit 1
fi

# Main menu
echo "What would you like to do?"
echo ""
echo "1. 🗺️  Generate market map (find 180+ businesses)"
echo "2. 📧  Send email batch (10 emails)"
echo "3. 📅  Check follow-ups due today"
echo "4. 📊  View analytics dashboard"
echo "5. 🚀  RUN EVERYTHING (full automation)"
echo ""
read -p "Enter choice [1-5]: " choice

case $choice in
    1)
        echo ""
        echo "${BLUE}Generating market map...${NC}"
        python3 tools/market_mapper.py --demo --limit 15
        echo ""
        echo "${GREEN}✅ Done! Check:${NC}"
        echo "  📁 maps/complete_map.html - Open in browser"
        echo "  📋 maps/action_plan_*.md - Your action plan"
        ;;

    2)
        echo ""
        echo "${BLUE}Preparing email batch...${NC}"
        python3 tools/auto_email_sender.py send --batch 10
        echo ""
        echo "${YELLOW}💡 This was a DRY RUN${NC}"
        echo "To actually send, run:"
        echo "  python3 tools/auto_email_sender.py send --batch 10 --send"
        ;;

    3)
        echo ""
        echo "${BLUE}Checking follow-ups...${NC}"
        python3 tools/auto_email_sender.py followup
        ;;

    4)
        echo ""
        echo "${BLUE}Opening analytics dashboard...${NC}"
        if [ -f "automation_data/dashboard.html" ]; then
            if command -v open &> /dev/null; then
                open automation_data/dashboard.html
            elif command -v xdg-open &> /dev/null; then
                xdg-open automation_data/dashboard.html
            else
                echo "Dashboard: automation_data/dashboard.html"
            fi
        else
            echo "No dashboard yet. Run full automation first (option 5)."
        fi
        ;;

    5)
        echo ""
        echo "${GREEN}🚀 RUNNING FULL AUTOMATION${NC}"
        echo ""

        # Step 1: Generate leads
        echo "${BLUE}Step 1/4: Generating leads...${NC}"
        python3 tools/automation_master.py --auto-run --batch-size 10
        echo ""

        # Step 2: Open map
        echo "${BLUE}Step 2/4: Opening market map...${NC}"
        if [ -f "maps/complete_map.html" ]; then
            if command -v open &> /dev/null; then
                open maps/complete_map.html
            elif command -v xdg-open &> /dev/null; then
                xdg-open maps/complete_map.html
            fi
        fi
        echo ""

        # Step 3: Prepare emails (dry run)
        echo "${BLUE}Step 3/4: Preparing email campaign...${NC}"
        python3 tools/auto_email_sender.py send --batch 10
        echo ""

        # Step 4: Show dashboard
        echo "${BLUE}Step 4/4: Generating analytics...${NC}"
        if [ -f "automation_data/dashboard.html" ]; then
            if command -v open &> /dev/null; then
                open automation_data/dashboard.html
            elif command -v xdg-open &> /dev/null; then
                xdg-open automation_data/dashboard.html
            fi
        fi
        echo ""

        echo "=========================================================================="
        echo "${GREEN}✅ AUTOMATION COMPLETE!${NC}"
        echo "=========================================================================="
        echo ""
        echo "📁 Files created:"
        echo "  • maps/complete_map.html - Visual map of all businesses"
        echo "  • automation_data/email_drafts/ - Ready-to-send emails"
        echo "  • automation_data/dashboard.html - Analytics dashboard"
        echo "  • automation_data/today_actions.txt - What to do today"
        echo ""
        echo "🎯 Next steps:"
        echo "  1. Review the market map"
        echo "  2. Send your first batch: ./automate.sh → option 2"
        echo "  3. Check follow-ups daily: ./automate.sh → option 3"
        echo ""
        ;;

    *)
        echo "Invalid choice!"
        exit 1
        ;;
esac

echo ""
echo "Done! Run ./automate.sh again anytime."
