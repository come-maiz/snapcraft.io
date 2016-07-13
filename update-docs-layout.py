#! /usr/bin/env python3

import glob
import frontmatter


doc_layout = 'documentation'


def update_layout_in_dir(directory, layout):
    """
    Update "layout" key in frontmatter of all markdown files in a directory
    """

    for markdown_file in glob.iglob(directory + '/**/*.md', recursive=True):
        print("updating " + markdown_file)
        document = frontmatter.load(markdown_file)  # Read file
        document['layout'] = layout  # Update layout in document
        frontmatter.dump(document, markdown_file)  # Write back to file


if __name__ == '__main__':
    print("in main")
    update_layout_in_dir('docs', doc_layout)
