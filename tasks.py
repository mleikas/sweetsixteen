from invoke import task


@task
def build(ctx):
    ctx.run("python3 src/utils/initialize_database.py")
