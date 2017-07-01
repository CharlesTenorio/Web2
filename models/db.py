# -*- coding: utf-8 -*-

#db = DAL('mysql://charlestenorios:sql162@cloud11.ny1.porta80.com.br/myplace_db')
#db = DAL('mysql://root:@localhost/myplace_local')
#bd_katanapg bd_katanamy
from datetime import  date
from gluon.tools import Auth
if not request.env.web2py_runtime_gae:
    db = DAL('postgres://postgres:sql162@localhost/bd_katanapg')

#  db =DAL('google:sql://condomino-171920:katanapg/bd_katanapg')
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    #

#db =DAL('postgres://postgres:sql162@localhost/bd_katanapg')
session.connect(request, response, db=db)
auth = Auth(globals(),db)
auth.define_tables()

UFS =['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PR','PB','PA','PE','PI','RJ','RN','RS','RO','RR','SC','SE','SP','TO','NT']


tblEmpresas = db.define_table('empresas',
                              Field('cnpj','string', length=80,  label= 'CNPJ', requires = [IS_NOT_EMPTY(error_message='campo obrigatório'), IS_NOT_IN_DB(db, 'empresas.cnpj', error_message='CNPJ já cadastrado')]  ),
                              Field('razao_social', 'string', length=100 , label= 'Razão Social', requires = IS_NOT_EMPTY(error_message='campo obrigatório')),
                              Field('fantasia', 'string', length=80,  label= 'Fantasia', requires = IS_NOT_EMPTY(error_message='campo obrigatório')),
                              Field('cep', 'string', length=10 , label= 'CEP', requires = IS_NOT_EMPTY(error_message='campo obrigatório')),
                              Field('endereco', 'string', length=80, label= 'Endereço', requires = IS_NOT_EMPTY(error_message='campo obrigatório')),
                              Field('bairro', 'string', length=80 , label= 'Bairro', requires = IS_NOT_EMPTY(error_message='campo obrigatório')),
                              Field('cidade', 'string', length=80, label= 'Cidade', requires = IS_NOT_EMPTY(error_message='campo obrigatório')),
                              Field('uf', 'string', length=2 , label= 'UF', requires=[IS_IN_SET(UFS),IS_NOT_EMPTY(error_message='campo obrigatório')]),
                              Field('latitude', 'string', length=50, requires = IS_NOT_EMPTY(error_message='campo obrigatório')),
                              Field('longitude', 'string', length=50, requires = IS_NOT_EMPTY(error_message='campo obrigatório')),
                              Field('qtd_ivas','integer' , label= 'Qtd de ivas', requires = IS_NOT_EMPTY(error_message='campo obrigatório')),
                              Field('status_empresa', 'string', length=30 , label= 'Status'),
                              Field('data_cadastro', 'date', default= date.today()),
                              Field('user_id', 'reference auth_user', default=auth.user_id,  readable=True, writable=False)
                              )


tblSetor= db.define_table('setores',
                           Field('id_empresa', 'integer', length=80, requires= IS_IN_DB(db, 'empresas.id', 'empresas.fantasia'), label='Empresa'),
                           Field('codigo_setor', 'string', length=20),
                           Field('setor', 'string', length=40),
                           Field('user_id', 'reference auth_user', default=auth.user_id,  readable=True, writable=False)
                          )

tblGrupo= db.define_table('grupos_ivas',
                           Field('id_empresa', 'integer', length=80, requires= IS_IN_DB(db, 'empresas.id', 'empresas.fantasia'), label='Empresa'),
                           Field('codigo_grupo', 'string', length=20),
                           Field('grupo', 'string', length=40),
                           Field('user_id', 'reference auth_user', default=auth.user_id,  readable=True, writable=False)
                          )

tblProduto = db.define_table('produtos',
                           Field('id_empresa', 'integer', length=80, requires= IS_IN_DB(db, 'empresas.id', 'empresas.fantasia'), label='Empresa'),
                           Field('codigo_de_barras', 'string', length=40, requires = [IS_NOT_EMPTY(error_message='campo obrigatório'), IS_NOT_IN_DB(db, 'produtos.codigo_de_barras', error_message='CNPJ já cadastrado')]),
                           Field('descricao', 'string', length=40),
                           Field('id_grupo_iva', 'integer', length=80, requires= IS_IN_DB(db, 'grupos_ivas.id', 'grupos_ivas.grupo'), label='Grupo IVA'),
                           Field('id_setor', 'integer', length=80, requires= IS_IN_DB(db, 'setores.id', 'setores.setor'), label='Grupo'),
                           Field('url_video', 'string', length= 200, requires=IS_NOT_EMPTY(error_message='campo obrigatório')),
                           Field('url_img', 'string',  length= 200, requires=IS_NOT_EMPTY(error_message='campo obrigatório')),
                           Field('user_id', 'reference auth_user', default=auth.user_id,  readable=True, writable=False)
                         )

tblIvas = db.define_table('ivas',
                          Field('id_empresa', 'integer', length=80,  requires=IS_IN_DB(db, 'empresas.id', 'empresas.fantasia'), label='Empresa'),
                          Field('descricao', 'string', length=40, label='Descrição', requires=  IS_NOT_EMPTY(error_message='campo obrigatório')  ),
                          Field('modelo', 'string', length=40, label='Modelo' , requires=  IS_NOT_EMPTY(error_message='campo obrigatório')),
                          Field('serial', 'string', length=40, label='Serial'),
                          Field('id_grupo_iva', 'integer', length=80, requires=IS_IN_DB(db, 'grupos_ivas.id', 'grupos_ivas.grupo'), label='Grupo IVA'),
                          Field('id_setor', 'integer', length=80, requires=IS_IN_DB(db, 'setores.id', 'setores.setor'), label='Grupo'),
                          )



