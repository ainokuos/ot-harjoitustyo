from invoke import task

@task
def test(ctx):
	ctx.run("pytest src" )

@task
def start(ctx):
	ctx.run("python3 src/index.py")


@task
def build(ctx):
	ctx.run("python3 src/initialize_database.py")


@task
def coverage(ctx):
	ctx.run("coverage run --branch -m pytest src")

@task
def coverage_report(ctx):
	ctx.run("coverage html")

@task
def lint(ctx):
	ctx.run("pylint src")
