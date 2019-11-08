import redminelib
import click
import keyring

@click.group()
def cli():
    pass

def connect():
    redmine = redminelib.Redmine('https://redmine.isdc.unige.ch/', 
                       username=keyring.get_password('redmine', 'username'), 
                       password=keyring.get_password('redmine', 'password'))
    return redmine

@cli.command("list")
@click.option("--project-name", default="INTEGRAL")
@click.option("--me", default="Volodymyr SAVCHENKO")
def list_active(project_name, me):
    r = connect()
    project = r.project.get(project_name)
    click.echo(project.id)
    
    for issue in project.issues:
        #print(issue, issue.assigned_to)
        try:
            if issue.assigned_to.name.lower() == me.lower():
                click.echo("issue: %s of %s, %s"%(issue,issue.created_on, issue.priority))
                #print("-- to", issue.created_on)
                #print("-- to", issue.assigned_to.__class__)
                #print("-- to", issue.assigned_to.name.__class__)
        except redminelib.exceptions.ResourceAttrError:
            pass
        except Exception as e:
            click.echo("unassigned: %s; %s"% (issue, repr(e)))


if __name__ == "__main__":
    cli()
