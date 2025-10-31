/**
 * LocalSearchPro - Professional Website JavaScript
 * Handles navigation, form submission, and interactive elements
 */

(function() {
    'use strict';

    // Smooth scrolling for navigation links
    function initSmoothScrolling() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                const href = this.getAttribute('href');
                if (href === '#') return;

                e.preventDefault();
                const target = document.querySelector(href);

                if (target) {
                    const navHeight = document.querySelector('.header').offsetHeight;
                    const targetPosition = target.offsetTop - navHeight;

                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });

                    // Close mobile menu if open
                    const navMenu = document.querySelector('.nav-menu');
                    if (navMenu.classList.contains('active')) {
                        navMenu.classList.remove('active');
                    }
                }
            });
        });
    }

    // Mobile menu toggle
    function initMobileMenu() {
        const mobileToggle = document.querySelector('.mobile-toggle');
        const navMenu = document.querySelector('.nav-menu');

        if (mobileToggle && navMenu) {
            mobileToggle.addEventListener('click', function() {
                navMenu.classList.toggle('active');
                this.classList.toggle('active');
            });

            // Close menu when clicking outside
            document.addEventListener('click', function(e) {
                if (!e.target.closest('.nav-container')) {
                    navMenu.classList.remove('active');
                    mobileToggle.classList.remove('active');
                }
            });
        }
    }

    // FAQ accordion functionality
    function initFAQ() {
        const faqItems = document.querySelectorAll('.faq-item');

        faqItems.forEach(item => {
            const question = item.querySelector('.faq-question');
            const answer = item.querySelector('.faq-answer');

            if (question && answer) {
                // Set initial state
                answer.style.display = 'none';

                question.addEventListener('click', function() {
                    const isActive = item.classList.contains('active');

                    // Close all other FAQ items
                    faqItems.forEach(otherItem => {
                        if (otherItem !== item) {
                            otherItem.classList.remove('active');
                            const otherAnswer = otherItem.querySelector('.faq-answer');
                            if (otherAnswer) {
                                otherAnswer.style.display = 'none';
                            }
                        }
                    });

                    // Toggle current item
                    item.classList.toggle('active');
                    answer.style.display = isActive ? 'none' : 'block';
                });
            }
        });
    }

    // Form submission handler
    function initContactForm() {
        const form = document.getElementById('auditForm');

        if (form) {
            form.addEventListener('submit', function(e) {
                e.preventDefault();

                // Get form data
                const formData = new FormData(form);
                const data = {
                    name: formData.get('name'),
                    business: formData.get('business'),
                    email: formData.get('email'),
                    phone: formData.get('phone'),
                    googleUrl: formData.get('googleUrl'),
                    message: formData.get('message')
                };

                // Validate required fields
                if (!data.name || !data.business || !data.email || !data.phone) {
                    alert('Please fill in all required fields.');
                    return;
                }

                // Email validation
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(data.email)) {
                    alert('Please enter a valid email address.');
                    return;
                }

                // Show loading state
                const submitButton = form.querySelector('.btn-submit');
                const originalText = submitButton.textContent;
                submitButton.textContent = 'Sending...';
                submitButton.disabled = true;

                // TODO: Replace with your actual form handling
                // Option 1: Use a service like Formspree, Basin, or Getform
                // Option 2: Send to your own backend API
                // Option 3: Use email.js or similar service

                // Example with timeout (replace with actual submission)
                setTimeout(() => {
                    console.log('Form submitted:', data);

                    // Show success message
                    alert('Thank you! We\'ll send your free audit report within 24 hours.');

                    // Reset form
                    form.reset();
                    submitButton.textContent = originalText;
                    submitButton.disabled = false;

                    // Scroll to top
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                }, 1000);

                // PRODUCTION: Replace setTimeout above with actual form submission
                // Example using fetch API:
                /*
                fetch('YOUR_FORM_ENDPOINT_URL', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data)
                })
                .then(response => response.json())
                .then(result => {
                    alert('Thank you! We\'ll send your free audit report within 24 hours.');
                    form.reset();
                    submitButton.textContent = originalText;
                    submitButton.disabled = false;
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Oops! Something went wrong. Please call us directly.');
                    submitButton.textContent = originalText;
                    submitButton.disabled = false;
                });
                */
            });
        }
    }

    // Intersection Observer for scroll animations
    function initScrollAnimations() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        // Select elements to animate
        const animatedElements = document.querySelectorAll(
            '.service-item, .result-card, .pricing-card, .problem-item, .timeline-item'
        );

        animatedElements.forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(el);
        });
    }

    // Sticky header shadow on scroll
    function initStickyHeader() {
        const header = document.querySelector('.header');
        let lastScroll = 0;

        window.addEventListener('scroll', function() {
            const currentScroll = window.pageYOffset;

            if (currentScroll > 50) {
                header.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)';
            } else {
                header.style.boxShadow = '0 1px 2px 0 rgba(0, 0, 0, 0.05)';
            }

            lastScroll = currentScroll;
        });
    }

    // Phone number click tracking (for analytics)
    function initPhoneTracking() {
        const phoneLinks = document.querySelectorAll('a[href^="tel:"]');

        phoneLinks.forEach(link => {
            link.addEventListener('click', function() {
                // Track phone click event
                if (typeof gtag !== 'undefined') {
                    gtag('event', 'phone_click', {
                        'event_category': 'engagement',
                        'event_label': 'Phone Number Clicked'
                    });
                }
                console.log('Phone number clicked:', this.href);
            });
        });
    }

    // Email link tracking (for analytics)
    function initEmailTracking() {
        const emailLinks = document.querySelectorAll('a[href^="mailto:"]');

        emailLinks.forEach(link => {
            link.addEventListener('click', function() {
                // Track email click event
                if (typeof gtag !== 'undefined') {
                    gtag('event', 'email_click', {
                        'event_category': 'engagement',
                        'event_label': 'Email Link Clicked'
                    });
                }
                console.log('Email link clicked:', this.href);
            });
        });
    }

    // CTA button tracking
    function initCTATracking() {
        const ctaButtons = document.querySelectorAll('.btn-primary, .pricing-cta');

        ctaButtons.forEach(button => {
            button.addEventListener('click', function() {
                if (typeof gtag !== 'undefined') {
                    gtag('event', 'cta_click', {
                        'event_category': 'engagement',
                        'event_label': this.textContent.trim()
                    });
                }
                console.log('CTA clicked:', this.textContent.trim());
            });
        });
    }

    // Initialize all functions when DOM is ready
    function init() {
        initSmoothScrolling();
        initMobileMenu();
        initFAQ();
        initContactForm();
        initScrollAnimations();
        initStickyHeader();
        initPhoneTracking();
        initEmailTracking();
        initCTATracking();
    }

    // Wait for DOM to be fully loaded
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
