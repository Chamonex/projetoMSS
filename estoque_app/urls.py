from django.urls import path
from estoque_app import views

urlpatterns = [
    # Página inicial
    path("", views.home, name="home"),
    
    # Gerenciar usuários
    path("perfis/", views.perfis, name="perfis"),
    
    # Editar usuário (rota dinâmica com ID do usuário)
    path("editUser/<int:user_id>/", views.edit_user, name="editUser"),
    
    # Remover usuário (rota dinâmica com ID do usuário)
    path("deleteUser/", views.delete_user, name="deleteUser"),

    # Criar usuário
    path("createUser/", views.create_user, name="createUser"),

     # Página produtos
     path("produtos/", views.produtos, name="produtos"),

    # Página para cadastrar usuário na plataforma
     path("cadastro/", views.signup, name="cadastro"),

    # Página para logar usuário na plataforma
     path("login/", views.login, name="login"),

    # Página para cadastrar produto
    path("registerProduct/", views.registerProduct, name="registerProduct"),

    # Página de estoque
    path("stock/", views.stock, name="stock"),

    # Página de deletar produto
    path("deleteProduct/", views.deleteProduct, name="deleteProduct"),

    # Página para editar estoque
    path("editStock/", views.changeStock, name="changeStock"),
]
