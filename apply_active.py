import os
import re

files_to_update = ['about.html', 'contact.html', 'gallery.html', 'home2.html', 'parts.html', 'project-page.html', 'restoration.html', 'services.html', 'index.html']

style_to_remove = r'\s*style="color:\s*var\(--color-accent\);\s*border-bottom:\s*2px\s*solid\s*var\(--color-accent\);\s*padding-bottom:\s*2px;"'

# Also might be on a single line
style_to_remove_inline = r'\s*style="color: var\(--color-accent\); border-bottom: 2px solid var\(--color-accent\); padding-bottom: 2px;"'

js_snippet = """
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
                if (href === currentPage) {
                    link.classList.add('text-accent');
                    link.classList.remove('text-primary', 'text-secondary');
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
"""

# We want to insert js_snippet right before // Marquee duplication or });
# We will use regex to find the insertion point

insertion_regex = re.compile(r'(\s*// Marquee duplication[^\n]*\n\s*.*?\n\s*}\);\s*</script>)', re.DOTALL)
# Or if `// Marquee duplication` doesn't exist just look for `}\);\s*</script>`
fallback_regex = re.compile(r'(\s*}\);\s*</script>)', re.DOTALL)

for file in files_to_update:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove hardcoded styles
        new_content = re.sub(style_to_remove, '', content)
        new_content = re.sub(style_to_remove_inline, '', new_content)

        # Inject JS if not already there
        if "Active Nav State Automation" not in new_content:
            if insertion_regex.search(new_content):
                new_content = insertion_regex.sub(lambda m: js_snippet + m.group(1), new_content)
            elif fallback_regex.search(new_content):
                new_content = fallback_regex.sub(lambda m: js_snippet + m.group(1), new_content)
            else:
                print(f"Could not find insertion point in {file}")

        if content != new_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")
        else:
            print(f"Skipped {file} (no changes)")
            
    except Exception as e:
        print(f"Failed on {file}: {e}")

