from datetime import datetime
from fabric.api import  * #env, run, sudo

env.use_ssh_config =  True
env.hosts =['kinoko']

@task
def uptime():
    ""
    run('uptime')
    
@task
def reboot():
    "Reboot Apache2 server."
    run("apachectl graceful")

@task
def deploy():
    ara = datetime.now()
    stag = ara.strftime("Distribuit_%Y-%m-%d--%H-%M-%S")
    local('./manage.py collectstatic --noinput')
    local('git add .')
    with settings(warn_only=True):
         local('git commit -m %s' % stag )
    local('git tag %s ' % stag )
    local('git push' ) 
    with cd('/srv/tuma.cat/vm0/'):
        run('git pull')
        run('./manage.py migrate')
    
    run("apachectl graceful")

@task
def espai():
    print("          -- Ocupat en /srv -- ")    
    with hide('running'):
        with cd('/srv/'):
            run('du -hs *')
            print("              -----   ")    
            run('du -hs')
    print("          -- Detall de tuma.cat -- ")    
    with cd('/srv/tuma.cat/'):
        with hide('running'):
            run('du -hs *')
            print("              -----   ")    
            run('du -hs')
    print("          -- ESPAI LLIURE -- ")
    with hide('running'):
        run( "df -h | grep 'Filesystem'")    
        run( "df -h | grep '/dev/xvda2'")    
