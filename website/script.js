// Smooth scrolling for anchor links
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

// Form submission handler (you'll need to configure this with your backend)
const contactForm = document.querySelector('.contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();

        // Get form data
        const formData = new FormData(this);
        const data = Object.fromEntries(formData);

        // Here you would typically send this to your backend
        // For now, we'll just log it and show an alert
        console.log('Form submitted:', data);

        // Show success message
        alert('Thank you! We\'ll send your free audit report within 24 hours.');

        // Reset form
        this.reset();

        // TODO: Replace this with actual form submission to your backend
        // Example:
        // fetch('/api/submit-audit-request', {
        //     method: 'POST',
        //     headers: { 'Content-Type': 'application/json' },
        //     body: JSON.stringify(data)
        // })
        // .then(response => response.json())
        // .then(data => {
        //     alert('Thank you! We\'ll send your free audit report within 24 hours.');
        //     this.reset();
        // })
        // .catch(error => {
        //     alert('Oops! Something went wrong. Please call us instead.');
        // });
    });
}

// Add animation on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe elements for animation
document.querySelectorAll('.service-card, .result-card, .pricing-card, .problem-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
});

// Mobile menu toggle (if you add a hamburger menu later)
const createMobileMenu = () => {
    const navbar = document.querySelector('.navbar');
    const navLinks = document.querySelector('.nav-links');

    // Only create mobile menu on small screens
    if (window.innerWidth <= 768) {
        if (!document.querySelector('.mobile-menu-toggle')) {
            const menuToggle = document.createElement('button');
            menuToggle.className = 'mobile-menu-toggle';
            menuToggle.innerHTML = '☰';
            menuToggle.style.cssText = 'font-size: 1.5rem; background: none; border: none; cursor: pointer; display: block;';

            menuToggle.addEventListener('click', () => {
                navLinks.classList.toggle('active');
            });

            navbar.querySelector('.container').insertBefore(menuToggle, navLinks);
        }
    }
};

// Initialize mobile menu on load and resize
window.addEventListener('load', createMobileMenu);
window.addEventListener('resize', createMobileMenu);

// Add sticky header effect
let lastScroll = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll > 100) {
        navbar.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
    } else {
        navbar.style.boxShadow = '0 1px 3px rgba(0,0,0,0.1)';
    }

    lastScroll = currentScroll;
});
