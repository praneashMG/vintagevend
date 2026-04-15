const fs = require('fs');
const path = require('path');

const filesToUpdate = ['about.html', 'contact.html', 'gallery.html', 'home2.html', 'parts.html', 'project-page.html', 'restoration.html', 'services.html', 'index.html'];

const styleToRemove = /\s*style="color:\s*var\(--color-accent\);\s*border-bottom:\s*2px\s*solid\s*var\(--color-accent\);\s*padding-bottom:\s*2px;"/g;

const jsSnippet = `
            // --- Active Nav State Automation ---
            const currentPage = window.location.pathname.split('/').pop() || 'index.html';
            
            // 1. Desktop Nav
            document.querySelectorAll('.hidden.lg\\\\:flex .nav-link, .hidden.lg\\\\:flex .dropdown-menu a').forEach(link => {
                const href = link.getAttribute('href');
                if (href === currentPage) {
                    link.classList.add('active');
                    link.style.color = 'var(--color-accent)';
                    // If it's in a dropdown, highlight the parent dropdown button too
                    const dropdown = link.closest('.dropdown-wrapper');
                    if (dropdown) {
                        const toggle = dropdown.querySelector('.dropdown-toggle');
                        if (toggle) {
                            toggle.classList.add('active');
                            toggle.style.color = 'var(--color-accent)';
                        }
                    }
                }
            });

            // 2. Mobile Nav
            document.querySelectorAll('#mobile-menu-drawer a, #mobile-menu-drawer button').forEach(link => {
                const href = link.getAttribute('href');
                let isMatch = false;
                if (href === currentPage) {
                    isMatch = true;
                }
                
                if (isMatch) {
                    link.classList.add('text-accent');
                    link.classList.remove('text-primary', 'text-secondary', 'text-primary-text');
                    // For mobile dropdown
                    const parentMenu = link.closest('#mobile-homes-menu');
                    if(parentMenu){
                       const toggle = document.getElementById('mobile-homes-toggle');
                       if(toggle){
                           toggle.classList.add('text-accent');
                           toggle.classList.remove('text-primary');
                       }
                    }
                }
            });
`;

const insertionRegexList = [
    /(\s*\/\/\s*Marquee duplication[^\n]*\n\s*.*?\n\s*}\);\s*<\/script>)/g,
    /(\s*}\);\s*<\/script>)/g
];

filesToUpdate.forEach(file => {
    try {
        const filePath = path.join(__dirname, file);
        let content = fs.readFileSync(filePath, 'utf8');
        let newContent = content.replace(styleToRemove, '');

        if (!newContent.includes('Active Nav State Automation')) {
            let matched = false;
            for (let regex of insertionRegexList) {
                if (regex.test(newContent)) {
                    // reset regex index
                    regex.lastIndex = 0;
                    newContent = newContent.replace(regex, (match, p1) => jsSnippet + p1);
                    matched = true;
                    break;
                }
            }
            if (!matched) console.log(`Could not find insertion point in ${file}`);
        }

        if (content !== newContent) {
            fs.writeFileSync(filePath, newContent, 'utf8');
            console.log(`Updated ${file}`);
        } else {
            console.log(`Skipped ${file} (no changes)`);
        }
    } catch (e) {
        console.error(`Failed on ${file}: ${e.message}`);
    }
});
