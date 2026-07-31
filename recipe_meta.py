import sys

import frontmatter

with open(sys.argv[1], "r") as f:
    post = frontmatter.load(f)
    meta = post.metadata

    for k, v in meta.items():
        print(f"{k}: {v}")
