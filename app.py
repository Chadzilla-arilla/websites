#!/usr/bin/env python3
"""
Script to generate MDwiki files from Jekyll site conversion
This script creates all the necessary files and directories for the MDwiki conversion
"""

import os
import shutil

def create_directories():
    """Create necessary directories"""
    directories = ['posts', 'people']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    print("✓ Created directories: posts, people")

def write_file(filename, content):
    """Write content to file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Created {filename}")

def main():
    print("🚀 Converting Jekyll site to MDwiki v0.6.4...")
    print()
    
    # Create directories first
    create_directories()
    
    # index.html (MDwiki Loader)
    index_html = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>club toilet presents: websites</title>
</head>
<body>
    <div id="md-content">
        <!-- This will be replaced by MDwiki -->
    </div>
    <script src="https://www.mdwiki.info/dist/mdwiki.js"></script>
</body>
</html>'''
    
    # index.md (Main Content)
    index_md = '''# club toilet presents: websites

## welcome to the studio

this is site  
bookmark for next time  
inquire within: [an email address?](mailto:xggm8ybptt@privaterelay.appleid.com)  
read the [privacy policy](privacy.md)'''
    
    # navigation.md
    navigation_md = '''# Website Navigation

[Home](index.md)
[Posts](posts.md)
[People](people.md)
[Privacy](privacy.md)'''
    
    # privacy.md
    privacy_md = '''# Privacy Policy

**Effective Date:** 19 May 2025

This privacy policy applies to the iOS app **Barcodes by Club Toilet** (the "App") developed and published by **Club Toilet**.

## Information We Collect
We do **not collect, store, or transmit** any personal data.

## Camera Access
The App requests access to your device's camera **only to scan barcodes**. No images or video are saved, transmitted, or processed outside of your device. All barcode scanning occurs locally on your iPhone or iPad.

## Data Sharing
We do not collect or share any information with third parties. The App does not use analytics tools, advertising networks, tracking technologies, or external data services.

## Children's Privacy
This App is rated 4+ and may be used by children. However, the App does not collect, store, or transmit any personal information from users of any age. No user accounts or sign-in are required, and no data is shared with third parties.

## Changes to This Policy
If we make any changes to this Privacy Policy, we will update the version posted on this page. We encourage users to review this page periodically for the latest information.

## Contact
If you have any questions or concerns about this Privacy Policy, you may contact us at:  
[xggm8ybptt@privaterelay.appleid.com](mailto:xggm8ybptt@privaterelay.appleid.com)

Last updated: 19 May 2025

[Thou may'st venture forth unto our GitHub repository through yonder portal, which doth graciously bestow thee with a link most noble and true.](https://github.com/Chadzilla-arilla/websites)

[Home](index.md)'''
    
    # posts.md
    posts_md = '''# Posts

- [come one come yall](posts/2025-05-19-future-agenda.md) - May 19, 2025'''
    
    # posts/2025-05-19-future-agenda.md
    post_content = '''# come one come yall

*May 19, 2025*

take a seat

[← Back to Posts](../posts.md)'''
    
    # people.md
    people_md = '''# People

- [Site Admin](people/site-admin.md)'''
    
    # people/site-admin.md
    site_admin_md = '''# Site Admin

Contact: [xggm8ybptt@privaterelay.appleid.com](mailto:xggm8ybptt@privaterelay.appleid.com)

[← Back to People](../people.md)'''
    
    # GitHub workflow (optional)
    workflow_content = '''name: Deploy MDwiki to GitHub Pages

on:
  push:
    branches: ["master"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup Pages
        uses: actions/configure-pages@v5
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4'''
    
    # Write all files
    write_file('index.html', index_html)
    write_file('index.md', index_md)
    write_file('navigation.md', navigation_md)
    write_file('privacy.md', privacy_md)
    write_file('posts.md', posts_md)
    write_file('posts/2025-05-19-future-agenda.md', post_content)
    write_file('people.md', people_md)
    write_file('people/site-admin.md', site_admin_md)
    
    # Optionally create the updated GitHub workflow
    if not os.path.exists('.github'):
        os.makedirs('.github/workflows', exist_ok=True)
        write_file('.github/workflows/mdwiki-gh-pages.yml', workflow_content)
    
    print()
    print("🎉 Conversion complete!")
    print()
    print("Files created:")
    print("  📄 index.html (MDwiki loader)")
    print("  📄 index.md (main content)")
    print("  📄 navigation.md")
    print("  📄 privacy.md")
    print("  📄 posts.md")
    print("  📄 posts/2025-05-19-future-agenda.md")
    print("  📄 people.md")
    print("  📄 people/site-admin.md")
    if os.path.exists('.github/workflows/mdwiki-gh-pages.yml'):
        print("  📄 .github/workflows/mdwiki-gh-pages.yml")
    print()
    print("📋 Next steps:")
    print("  1. Remove old Jekyll files:")
    print("     - _config.yml")
    print("     - _layouts/ directory")
    print("     - _people/ directory")
    print("     - _posts/ directory")
    print("     - old index.html")
    print("     - privacy.html")
    print("  2. Test locally with: python -m http.server 8000")
    print("  3. Visit http://localhost:8000 to test")
    print("  4. Commit and push to GitHub")

def cleanup_jekyll_files():
    """Remove old Jekyll files (optional function)"""
    print("\n🧹 Cleaning up old Jekyll files...")
    
    files_to_remove = [
        '_config.yml',
        'privacy.html'
    ]
    
    directories_to_remove = [
        '_layouts',
        '_people', 
        '_posts'
    ]
    
    # Remove files
    for file in files_to_remove:
        if os.path.exists(file):
            os.remove(file)
            print(f"✓ Removed {file}")
    
    # Remove directories
    for directory in directories_to_remove:
        if os.path.exists(directory):
            shutil.rmtree(directory)
            print(f"✓ Removed {directory}/ directory")
    
    print("✓ Jekyll cleanup complete!")

if __name__ == "__main__":
    main()
    
    # Uncomment the line below if you want to automatically clean up Jekyll files
    # cleanup_jekyll_files()