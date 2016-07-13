#! /usr/bin/env python3

# Core modules
import glob

# 3rd party modules
import frontmatter


def update_layout_in_dir(directory, layout):
    """
    Update "layout" key in frontmatter of all markdown files in a directory
    """

    # Process each markdown file in turn
    for markdown_file in glob.iglob(directory + '/**/*.md', recursive=True):
        print("updating " + markdown_file)

        # Update frontmatter in file
        document = frontmatter.load(markdown_file)  # Read file
        document['layout'] = layout  # Update layout in frontmatter
        frontmatter.dump(document, markdown_file)  # Write back to file


if __name__ == '__main__':
    update_layout_in_dir(
        directory='docs',
        layout='documentation'
    )
