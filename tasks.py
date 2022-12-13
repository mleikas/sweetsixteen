from invoke import task


@task
def build(ctx):
    ctx.run("python3 src/utils/initialize_database.py")


@task(build)
def demo_build(ctx):
    ctx.run("python3 src/build_demo_db.py")


@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=True)


@task
def test(ctx):
    ctx.run("pytest src", pty=True)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)


@task
def lint(ctx):
    ctx.run("pylint --fail-under 9.0 src", pty=True)
