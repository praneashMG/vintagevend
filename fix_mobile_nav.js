const fs = require('fs');
const path = require('path');

const filesToUpdate = ['about.html', 'contact.html', 'gallery.html', 'home2.html', 'parts.html', 'project-page.html', 'restoration.html', 'services.html', 'index.html', 'partsdetails.html'];

filesToUpdate.forEach(file => {
    try {
        const filePath = path.join(__dirname, file);
        let content = fs.readFileSync(filePath, 'utf8');
        
        let newContent = content
            .replace(/class="text-primary font-semibold text-lg hover:text-accent py-2/g, 'class="text-primary-text font-semibold text-lg hover:text-accent py-2')
            .replace(/class="block text-primary font-semibold/g, 'class="block text-primary-text font-semibold');

        if (content !== newContent) {
            fs.writeFileSync(filePath, newContent, 'utf8');
            console.log(`Updated ${file}`);
        } else {
            console.log(`Skipped ${file} (no changes needed)`);
        }
    } catch (e) {
        console.error(`Failed on ${file}: ${e.message}`);
    }
});
