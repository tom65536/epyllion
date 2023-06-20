from __future__ import annotations

import nox

nox.options.sessions = ["lint", "docs"]


@nox.session
def lint(session: nox.Session) -> None:
    """
    Run the linter.
    """
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files", *session.posargs)


@nox.session
def docs(session: nox.Session) -> None:
    """
    Build the docs. Pass "--serve" to serve.
    """

    session.install(".[docs]")
    session.run("mkdocs", "build")
