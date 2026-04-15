const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

files.forEach(f => {
    let c = fs.readFileSync(f, 'utf8');
    let original = c;

    // Desktop logo replacement
    c = c.replace(/<a href="index\.html" class="text-2xl sm:text-3xl font-serif font-extrabold tracking-wide">\s*<span class="header-accent">Vintage<\/span><span class="text-accent">Vend<\/span>\s*<\/a>/g, 
        '<a href="index.html" class="text-2xl sm:text-3xl font-serif font-bold text-accent">VintageVend</a>'
    );
    
    // Mobile menu logo replacement
    c = c.replace(/<h3 class="text-2xl font-serif font-extrabold tracking-wide">\s*<span class="header-accent">Vintage<\/span><span class="text-accent">Vend<\/span>\s*<\/h3>/g, 
        '<h3 class="text-2xl sm:text-3xl font-serif font-bold text-accent">VintageVend</h3>'
    );
    // Might have newlines between spans in mobile menu
    c = c.replace(/<h3 class="text-2xl font-serif font-extrabold tracking-wide">\s*<span class="header-accent">Vintage<\/span><span class="text-accent">Vend<\/span>\s*<\/h3>/g, 
        '<h3 class="text-2xl sm:text-3xl font-serif font-bold text-accent">VintageVend</h3>'
    );
    
    // Fallback regex if spacing differs
    c = c.replace(/<a href="index\.html" class="[^"]*font-serif[^"]*">\s*<span[^>]*>Vintage<\/span>\s*<span[^>]*>Vend<\/span>\s*<\/a>/g, 
        '<a href="index.html" class="text-2xl sm:text-3xl font-serif font-bold text-accent">VintageVend</a>'
    );
    c = c.replace(/<h3 class="[^"]*font-serif[^"]*">\s*<span[^>]*>Vintage<\/span>\s*<span[^>]*>Vend<\/span>\s*<\/h3>/g, 
        '<h3 class="text-2xl sm:text-3xl font-serif font-bold text-accent">VintageVend</h3>'
    );

    if (c !== original) {
        fs.writeFileSync(f, c, 'utf8');
        console.log(`Updated logo in ${f}`);
    }
});
