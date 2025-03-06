"""Gestionnaire de Tâches avec Priorités
Crée une application console qui permet de:

Ajouter des tâches avec un titre, une description et un niveau de priorité (1-5)
Afficher toutes les tâches triées par priorité
Marquer des tâches comme terminées
Supprimer des tâches
Sauvegarder les tâches dans un fichier et les charger au démarrage"""
#Loops Practice
# project todo_list

#

list_of_task = []
task ={
    "titre":"doing grocery",
    "description ": "buy some milk and bread",
    "priorities": 5,
    "status": False
}
def show_menu () :
    print(list_of_task)
def add_a_task ():
    key = input("enter the title of the task")
    test = input("enter description of your task ")
