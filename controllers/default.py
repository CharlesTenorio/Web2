# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@auth.requires_membership('Adm')
#@auth.requires_login()
def cad_empresa():

    frmEpresas = SQLFORM(db.empresas)
    try:
        if frmEpresas.accepts(request.post_vars):
            response.flash = 'Empresa Cadastrada com Sucesso'
        elif frmEpresas.errors:
            response.flash= 'erro'
        else:
            response.flash= 'preencha o formulário'

    except:
      response.flash='erro ao cadastra'

    return dict(frmEpresas=frmEpresas)


@auth.requires_membership('Adm')
#@auth.requires_login()
def cad_setores():

    frmSetor = SQLFORM(db.setores)
    try:
        if frmSetor.accepts(request.post_vars):
            response.flash = 'Setor cadastrado com sucesso!'
        elif frmSetor.errors:
            response.flash= 'erro'
        else:
            response.flash= 'preencha o formulário'

    except:
      response.flash='erro ao cadastra'

    return dict(frmSetor=frmSetor)


@auth.requires_membership('Adm')
#@auth.requires_login()
def cad_grupo_iva():

    frmGrupoIva = SQLFORM(db.grupos_ivas)
    try:
        if frmGrupoIva.accepts(request.post_vars):
            response.flash = 'Setor cadastrado com sucesso!'
        elif frmGrupoIva.errors:
            response.flash= 'erro'
        else:
            response.flash= 'preencha o formulário'

    except:
      response.flash='erro ao cadastra'

    return dict(frmGrupoIva=frmGrupoIva)

@auth.requires_membership('Adm')
#@auth.requires_login()
def cad_produtos():

    frmProdutos = SQLFORM(db.produtos)
    try:
        if frmProdutos.accepts(request.post_vars):
            response.flash = 'Setor cadastrado com sucesso!'
        elif frmProdutos.errors:
            response.flash= 'erro'
        else:
            response.flash= 'preencha o formulário'

    except:
      response.flash='erro ao cadastra'

    return dict(frmProdutos=frmProdutos)

#@auth.requires_membership('Adm')
#@auth.requires_login()

@auth.requires_membership('Adm')
#@auth.requires_login()
def cad_ivas():

    frmIvas = SQLFORM(db.ivas)
    try:
        if frmIvas.accepts(request.post_vars):
            response.flash = 'Setor cadastrado com sucesso!'
        elif frmIvas.errors:
            response.flash= 'erro'
        else:
            response.flash= 'preencha o formulário'

    except:
      response.flash='erro ao cadastra'

    return dict(frmProdutos=frmIvas)

@auth.requires_membership('Adm')
def grid_empresas():
    grid_empresa = SQLFORM.grid(db.empresas,
                             deletable=False,
                             editable=True,
                             searchable=True,
                             create=False,
                                csv=False)

    return dict(gri_empresa=grid_empresa)

@auth.requires_membership('Adm')
def grid_setores():
    grid_setor = SQLFORM.grid(db.setores,
                                deletable=False,
                                editable=True,
                                searchable=True,
                                create=False,
                                csv=False)

    return dict(gri_setor=grid_setor)

@auth.requires_membership('Adm')
def grid_grupo_ivas():
    grid_grupo_iva = SQLFORM.grid(db.grupos_ivas,
                                deletable=False,
                                editable=True,
                                searchable=True,
                                create=False,
                                csv=False)

    return dict(gri_empresa=grid_grupo_iva)



@auth.requires_membership('Adm')
def grid_produtos():
    grid_produto = SQLFORM.grid(db.produtos,
                                deletable=False,
                                editable=True,
                                searchable=True,
                                create=False,
                                csv=False)

    return dict(grid_produto=grid_produto)












@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


