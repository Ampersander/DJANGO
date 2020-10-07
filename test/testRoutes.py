from django.core.urlresolvers import resolve
from django.test import TestCase
from lesTaches.views import home,about,task_listing,viewTask,newTask,editTask,deleteTask,viewUser,newUser,editUser,deleteUser,listUser


class HomePageTestContent(TestCase):

    routes = {
    "/list" :  task_listing,
    "/viewTask/testTask" :  viewTask,
    "/newTask" :  newTask,
    "/editTask/testTask" :  editTask,
    "/deleteTask/testTask" :  deleteTask,
    "/viewTask/testTask" :  deleteTask,
    "/viewUser/testUser" :  viewUser,
    "/newUser" :  newUser,
    "/editUser/testUser" :  editUser,
    "/deleteUser/testUser" :  deleteUser,
    "/listUser" :  listUser,
    }

    '''Test unitaire bidon'''
    def test_concatene(self):
        self.assertEqual("Bon"+"jour", "Bonjour")

    '''Test unitaire de la page accueil sur la racine du projet'''
    def test_root_url_resolves_to_home_view(self):
        for route,function in self.routes.items():
            found = resolve(route)
            self.assertEqual(found.func,function)

