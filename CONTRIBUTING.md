# Contributing

Welcome to paycheck, we love your inputs! Small, big, mini, micro, macro, we value them all! We want to make contributing to this project as easy and
transparent as possible. If you wish to contribute please first discuss the change
you wish to make via an issue, or email any other method with us. If you do not know on what to contribute, please send us a
small overview of your experience and optionally what you would like to learn. We will
get back to you as soon as possible with proposed issues.

## The pull request (PR) process

1. Open a new ticket (Feature Request/Change Request/Bug issue) by selecting the corresponding
   issue type when creating an issue, or comment on an existing issue.
2. Propose your plans and discuss them with the community on the issue.
3. Fork the repository and create a branch from `develop`.
4. Make the changes described in the issue.
5. Ensure that your code meets the quality standards - this could be done by running the
   `lint` and `test` commands as per module requirements.
6. Submit your merge request!
7. Usually we will enable the following merge options:
   1. "Delete source branch when merge request is accepted. "
   1. "Squash commits when merge request is accepted."
8. A maintainer will review your code and merge your code.

## Quality standards

- Backend code must have unit tests; we value quality, in order to keep a reliable software every feature must contain corresponding test suites.
- Python code must be compliant with the PEP 8 standard.
- SCSS code must be compliant with BEM.
- JavaScript code must be compliant with the eslint:recommended rules.
- In code documentation is required for every function or class that is not self-evident - we are not wizards.
- Documentation for every concept that is not self-evident, newly proposed, or integrated is required.
- A new changelog entry file should be generated using the script found in the changelog folder.
- Test pipelines must pass.
- Try to apply the **rule of 10s**: MRs should aim to have no more than 10 code files with more than 10 lines modified - this is a soft rule and can be broken if necessary.
  A code file doesn't include tests/css/text/migrations/translations/configuration/ etc.

## Any contributions you make will be under the MIT Software License

In short, when you submit code changes, your submissions are understood to be under
the same [MIT License](http://choosealicense.com/licenses/mit/) that covers the
project.

## Bug tracking

We use GH issues to track public bugs, internal bugs (temporarily, and would communicate as we decide on future process). You can report a bug by opening a new issue
at https://github.com/50-Course/paycheck/-/issues and selecting the Bug issue type.

**Great Bug Reports** tend to have:

- A quick summary and/or background.
- Steps to reproduce.
  - Be specific!
  - Give sample code if you can.
- What you expected would happen.
- What actually happens.
- Notes (possibly including why you think this might be happening, or stuff you tried
  that did not work)

People love thorough bug reports.

## Vulnerability

If you discover a security vulnerability within paycheck, please provide a detailed report to according to the [security policy](SECURITY.md). We will get back to you as soon as possible.

## Updating Documentation

The Paycheck documentation can be updated by editing Markdown files in the `docs` directory.
