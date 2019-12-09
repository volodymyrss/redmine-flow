import click

from .issues import commands as group1

from redmineflow.redmine import connect

@click.group()
@click.option("--project-name", default="INTEGRAL")
@click.pass_context
def entry_point(ctx, project_name):
    ctx.obj['redmine'] = connect()
    click.echo("connected to redmine {}".format(ctx.obj['redmine']))
    ctx.obj['project'] = ctx.obj['redmine'].project.get(project_name)
    click.echo("selected project {} as {}".format(project_name, ctx.obj['project']))


entry_point.add_command(group1.issues)
#entry_point.add_command(group2.version)


def main():
    entry_point(obj={})

if __name__ == "__main__":
    main()
