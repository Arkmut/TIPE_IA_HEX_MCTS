/*************************************************************************
                           Xxx  -  description
                             -------------------
    début                : $DATE$
    copyright            : (C) $YEAR$ par $AUTHOR$
    e-mail               : $EMAIL$
*************************************************************************/

//---------- Réalisation du module <Xxx> (fichier Xxx.cpp) ---------------

/////////////////////////////////////////////////////////////////  INCLUDE
//-------------------------------------------------------- Include système
#include <iostream>
using namespace std;
//------------------------------------------------------ Include personnel
#include "Ensemble.h"

#define MAP
///////////////////////////////////////////////////////////////////  PRIVE
//------------------------------------------------------------- Constantes

//------------------------------------------------------------------ Types

//---------------------------------------------------- Variables statiques

//------------------------------------------------------ Fonctions privées
//static type nom ( liste de paramètres )
// Mode d'emploi :
//
// Contrat :
//
// Algorithme :
//
//{
//} //----- fin de nom

//////////////////////////////////////////////////////////////////  PUBLIC
//---------------------------------------------------- Fonctions publiques
/*type Nom ( liste de paramètres )
// Algorithme :
//
{
} //----- fin de Nom*/




/// méthodes pour tester le constructeur par défaut

static void testConctructeurDefaut1()
// Algorithme : test constructeur par défaut sans paramètre
{
	Ensemble e;
	e.Afficher();
} //----- fin de testConctructeurDefaut1

static void testConctructeurDefaut2()
// Algorithme : test constructeur par défaut avec 0 comme parametre
{
	Ensemble e(0);
	e.Afficher();
} //----- fin de testConctructeurDefaut2

static void testConctructeurDefaut3()
// Algorithme : test constructeur par défaut avec 4 comme parametre
{
	Ensemble e(4);
	e.Afficher();
	
} //----- fin de testConctructeurDefaut3

static void testConctructeurDefaut()
// Algorithme : appelle les tests du constructeur par défaut 1, 2 et 3
{
	testConctructeurDefaut1();
	testConctructeurDefaut2();
	testConctructeurDefaut3();
	
} //----- fin de testConctructeurDefaut



/// méthodes pour tester le second constructeur
static void testSecondConstructeur1()
// Algorithme : test du second constructeur avec un tableau vide
{
	int tab[] = {};
	Ensemble e(tab, 0);
	e.Afficher();
} //----- fin de testSecondConstructeur1

static void testSecondConstructeur2()
// Algorithme : test du second constructeur avec {1,2,3}
{
	int tab[] = {1,2,3};
	Ensemble e(tab, 3);
	e.Afficher();
} //----- fin de testSecondConstructeur2

static void testSecondConstructeur3()
// Algorithme : test du second constructeur avec {1,2,3,4,5,6,7}
{
	int tab[] = {1,2,3,4,5,6,7};
	Ensemble e(tab, 7);
	e.Afficher();
	
} //----- fin de testSecondConstructeur3

static void testSecondConstructeur4()
// Algorithme : test du second constructeur avec {7,6,5,4,3,2,1}
{
	int tab[] = {7,6,5,4,3,2,1};
	Ensemble e(tab, 7);
	e.Afficher();
	
} //----- fin de testSecondConstructeur4

static void testSecondConstructeur5()
// Algorithme : test du second constructeur avec des doublons {7,7,7,4,3,4,1,7} 
{
	int tab[] = {7,7,7,7,7,4,3,4,1,4};
	Ensemble e(tab, 10);
	e.Afficher();
	
} //----- fin de testSecondConstructeur5


static void testSecondConstructeur6()
// Algorithme : test du second constructeur avec des cases vides 
{
	int tab[10];
	tab[0]=0;
	tab[1]=5;
	tab[2]=2;
	Ensemble e(tab, 3);
	e.Afficher();
	
} //----- fin de testSecondConstructeur6


static void testSecondConstructeur()
// Algorithme : appelle les tests du second constructeur 1, 2 et 3
{
	testSecondConstructeur1();
	testSecondConstructeur2();
	testSecondConstructeur3();
	testSecondConstructeur4();
	testSecondConstructeur5();
	testSecondConstructeur6();
} //----- fin de testSecondConstructeur




int main ()
{
	//testConctructeurDefaut();
	//testSecondConstructeur();
	int tab[] = {1,2,5,4};
	Ensemble e(tab, 4);
	e.Afficher();
	e.Ajuster(10);
	e.Afficher();
	e.Retirer(1);
	e.Afficher();

	return 0;
} //----- fin de main


