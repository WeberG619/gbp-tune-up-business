// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Form submission handling
const contactForm = document.getElementById('contactForm');

if (contactForm) {
    contactForm.addEventListener('submit', async function(e) {
        e.preventDefault();

        const formData = {
            businessName: document.getElementById('businessName').value,
            contactName: document.getElementById('contactName').value,
            phone: document.getElementById('phone').value,
            email: document.getElementById('email').value,
            message: document.getElementById('message').value,
            timestamp: new Date().toISOString(),
            source: 'website_contact_form'
        };

        // Get submit button
        const submitBtn = contactForm.querySelector('.btn-submit');
        const originalText = submitBtn.textContent;

        // Show loading state
        submitBtn.textContent = 'Sending...';
        submitBtn.disabled = true;

        try {
            // Option 1: Send to Netlify Forms (if using Netlify)
            if (window.location.hostname.includes('netlify.app')) {
                const response = await fetch('/', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: new URLSearchParams(formData).toString()
                });

                if (response.ok) {
                    showSuccess();
                } else {
                    throw new Error('Form submission failed');
                }
            }
            // Option 2: Email to your address (requires backend)
            else {
                // For now, just save to localStorage and show success
                // You can later integrate with email service (SendGrid, Mailgun, etc.)
                saveLeadLocally(formData);
                showSuccess();
            }

        } catch (error) {
            console.error('Form submission error:', error);
            showError();
        } finally {
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
        }
    });
}

function showSuccess() {
    const form = document.getElementById('contactForm');
    const formWrapper = form.parentElement;

    formWrapper.innerHTML = `
        <div style="text-align: center; padding: 60px 40px; background: rgba(16, 185, 129, 0.1); border-radius: 1rem; border: 2px solid #10b981;">
            <svg style="width: 64px; height: 64px; margin: 0 auto 20px; color: #10b981;" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/>
                <path d="M8 12L11 15L16 9" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
            <h3 style="font-size: 24px; margin-bottom: 12px; font-weight: 700; color: #111827;">Thank You!</h3>
            <p style="color: #4B5563; font-size: 16px; line-height: 1.7; max-width: 400px; margin: 0 auto;">
                I'll analyze your Google Business Profile and send you a detailed audit report within 24 hours.
            </p>
            <p style="margin-top: 20px; font-size: 14px; color: #6B7280;">
                Check your email (and spam folder) for my response.
            </p>
            <a href="/" style="display: inline-block; margin-top: 30px; padding: 12px 24px; background: #2563eb; color: white; text-decoration: none; border-radius: 0.75rem; font-weight: 600;">
                Back to Home
            </a>
        </div>
    `;

    // Track conversion (if using analytics)
    if (typeof gtag !== 'undefined') {
        gtag('event', 'generate_lead', {
            'event_category': 'contact',
            'event_label': 'form_submission'
        });
    }
}

function showError() {
    // Get contact info from the page
    const phone = document.querySelector('.footer-text:nth-of-type(2)')?.textContent || '[YOUR PHONE]';
    const email = document.querySelector('.footer-text:nth-of-type(3)')?.textContent || '[YOUR EMAIL]';
    alert(`There was an error submitting the form. Please call ${phone} or email ${email} directly.`);
}

function saveLeadLocally(data) {
    // Save to localStorage for now
    const leads = JSON.parse(localStorage.getItem('gbp_leads') || '[]');
    leads.push(data);
    localStorage.setItem('gbp_leads', JSON.stringify(leads));

    // Also send to console for debugging
    console.log('New lead captured:', data);

    // In production, you'd send this to your backend/email service
    // Example: Send to Zapier webhook, Google Sheets API, or email service
}

// Animate elements on scroll (optional enhancement)
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe cards and sections for fade-in animation
document.querySelectorAll('.problem-card, .service-card, .result-card, .pricing-card, .faq-item').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
});

// Phone number formatting
const phoneInput = document.getElementById('phone');
if (phoneInput) {
    phoneInput.addEventListener('input', function(e) {
        let value = e.target.value.replace(/\D/g, '');
        if (value.length > 0) {
            if (value.length <= 3) {
                value = `(${value}`;
            } else if (value.length <= 6) {
                value = `(${value.slice(0, 3)}) ${value.slice(3)}`;
            } else {
                value = `(${value.slice(0, 3)}) ${value.slice(3, 6)}-${value.slice(6, 10)}`;
            }
        }
        e.target.value = value;
    });
}

// Add active state to nav on scroll
window.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('section[id]');
    const scrollY = window.pageYOffset;

    sections.forEach(section => {
        const sectionHeight = section.offsetHeight;
        const sectionTop = section.offsetTop - 100;
        const sectionId = section.getAttribute('id');
        const navLink = document.querySelector(`.nav a[href="#${sectionId}"]`);

        if (navLink && scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            document.querySelectorAll('.nav-link').forEach(link => {
                link.style.color = '#4b5563';
            });
            navLink.style.color = '#2563eb';
        }
    });
});

// Export leads function (for admin use)
function exportLeads() {
    const leads = JSON.parse(localStorage.getItem('gbp_leads') || '[]');
    if (leads.length === 0) {
        alert('No leads to export');
        return;
    }

    const csv = convertToCSV(leads);
    downloadCSV(csv, 'website_leads.csv');
}

function convertToCSV(data) {
    if (data.length === 0) return '';

    const headers = Object.keys(data[0]);
    const rows = data.map(obj =>
        headers.map(header => `"${obj[header] || ''}"`).join(',')
    );

    return [headers.join(','), ...rows].join('\n');
}

function downloadCSV(csv, filename) {
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    window.URL.revokeObjectURL(url);
}

// Make exportLeads available globally (for admin console use)
window.exportLeads = exportLeads;

// Log to console for admin
console.log('%cApex Local Marketing - Admin Tools', 'font-size: 16px; font-weight: bold; color: #2563eb;');
console.log('Type exportLeads() to download all form submissions as CSV');
