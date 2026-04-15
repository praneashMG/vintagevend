const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

files.forEach(f => {
    let c = fs.readFileSync(f, 'utf8');
    let original = c;

    // Desktop
    c = c.replace(/<button onclick="alert\('Login demo[^\n\r]*?'\)" class="w-full text-left">([\s\S]*?)<\/button>/g, 
        '<a href="login.html" class="w-full text-left">$1</a>'
    );
    c = c.replace(/<button onclick="alert\('Signup demo[^\n\r]*?'\)" class="w-full text-left">([\s\S]*?)<\/button>/g, 
        '<a href="signup.html" class="w-full text-left">$1</a>'
    );

    // Mobile specific format using robust matching
    c = c.replace(/<button([^>]*?)>\s*<i class="fa-solid fa-right-to-bracket"><\/i> Login\s*<\/button>/g, 
        (match, p1) => {
            if(p1.includes('flex-1') || p1.includes('dropdown-toggle')===false){
                return `<a href="login.html"${p1}>\n                        <i class="fa-solid fa-right-to-bracket"></i> Login\n                    </a>`;
            }
            return match;
        }
    );
    
    c = c.replace(/<button([^>]*?)>\s*<i class="fa-solid fa-user-plus"><\/i> Signup\s*<\/button>/g, 
        (match, p1) => {
            if(p1.includes('flex-1') || p1.includes('dropdown-toggle')===false){
                return `<a href="signup.html"${p1}>\n                        <i class="fa-solid fa-user-plus"></i> Signup\n                    </a>`;
            }
            return match;
        }
    );
    
    if (c !== original) {
        fs.writeFileSync(f, c, 'utf8');
        console.log(`Updated ${f}`);
    }
});
