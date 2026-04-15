import os
import re

files_to_update = ['about.html', 'contact.html', 'gallery.html', 'home2.html', 'parts.html', 'project-page.html', 'restoration.html', 'services.html']

# The replacement for the outer mobile buttons
regex_outer = re.compile(r'<div class="flex items-center lg:hidden space-x-4">.*?<button id="mobile-menu-open"[^>]*>.*?</div>', re.DOTALL)
replacement_outer = '''<div class="flex items-center lg:hidden space-x-4">
                 
                <button id="mobile-menu-open" class="icon-btn text-primary hover:text-accent p-1.5 rounded-full">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" /></svg>
                </button>
            </div>'''

# The replacement for the inner title / header of the drawer
regex_drawer_top = re.compile(r'<div class="flex justify-between items-center pb-4 border-b border-border">\s*<h3 class="text-[^"]+ font-serif font-bold text-accent">Menu</h3>\s*<button id="mobile-menu-close".*?</button>\s*</div>', re.DOTALL)
replacement_drawer_top = '''<div class="flex justify-between items-center pb-4 border-b border-border">
<h3 class="text-2xl font-serif font-extrabold tracking-wide">
                <span class="header-accent">Vintage</span><span class="text-accent">Vend</span>

</h3>                <button id="mobile-menu-close" class="text-primary hover:text-accent p-1.5 rounded-full"><svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg></button>
            </div>'''

# The replacement for the inner Title/Header could also match 	ext-xl font-serif font-bold text-accent">Navigation</h3> maybe? Let's make it broader.
regex_drawer_top = re.compile(r'<div class="flex justify-between items-center pb-4 border-b border-border">\s*<h3 class="[^"]*">[^<]+</h3>\s*<button id="mobile-menu-close".*?</button>\s*</div>', re.DOTALL)


# The replacement for Login and Signup
regex_login = re.compile(r'<!-- Login & Signup inside mobile header -->\s*<div class="pt-3 mt-2 border-t border-border">.*?</div>', re.DOTALL)
replacement_login = '''<!-- Login & Signup inside mobile header -->
               <div class="pt-3 mt-2 border-t border-border flex gap-3">
    
    <!-- Login -->
    <button class="flex-1 py-2.5 rounded-lg border border-accent text-accent hover:bg-accent hover:text-white transition font-medium flex items-center justify-center gap-2">
        <i class="fa-solid fa-right-to-bracket"></i> Login
    </button>

    <!-- Signup -->
    <button class="flex-1 py-2.5 rounded-lg border border-accent text-accent hover:bg-accent hover:text-white transition font-medium flex items-center justify-center gap-2">
        <i class="fa-solid fa-user-plus"></i> Signup
    </button>

</div>'''

# The replacement for Bottom Icons
regex_bottom = re.compile(r'<div class="bottom-icons pt-4 border-t border-border mt-4 flex justify-around">.*?</div>', re.DOTALL)
replacement_bottom = '''<div class="bottom-icons pt-4 border-t border-border mt-4 flex justify-center items-center gap-8">

    <!-- Theme Toggle (same style as navbar) -->
    <button id="mobile-theme-toggle" class="icon-btn text-primary hover:text-accent p-1.5 rounded-full transition duration-200">
        <svg class="w-6 h-6 light-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z">
            </path>
        </svg>
        <svg class="w-6 h-6 dark-icon hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z">
            </path>
        </svg>
    </button>

    <!-- RTL -->
    <button id="mobile-lang-icon" class="icon-btn text-primary hover:text-accent p-1.5 rounded-full transition duration-200">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"/>
        </svg>
    </button>

</div>'''


for file in files_to_update:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = regex_outer.sub(replacement_outer, content)
        new_content = regex_drawer_top.sub(replacement_drawer_top, new_content)
        new_content = regex_login.sub(replacement_login, new_content)
        new_content = regex_bottom.sub(replacement_bottom, new_content)

        if content != new_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")
        else:
            print(f"Skipped {file} (no matches or already updated)")
            
    except Exception as e:
        print(f"Failed on {file}: {e}")

