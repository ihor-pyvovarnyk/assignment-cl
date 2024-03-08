# Assignment-cl

## Install

```bash
make activate_venv
make install
```

## Run

```bash
python cli.py --input-file=data/commit_urls.txt --output-dir=output
```

### Notes

* Since some repos are named as `core`, decided to use file naming schema like `{account}_{project}_{commit_hash}.patch` where applicable
* For a couple of example commits, wasn't able to find anywhere a link to the repository to clone it but found the same repos in GitHub, so trying to clone it from there
  * Got the commit URL from `git.gluster.org`, the referenced commit was not available in the GitHub repo of the same project 