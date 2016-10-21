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
//------------------------------------------------------ Include personnel
#include "Ensemble.h"
using namespace std;

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

static void testConctructeurDefaut1()
{
	Ensemble e();
	//e.Afficher();
} //----- fin de testConctructeurDefaut1

static void testConctructeurDefaut2()
{
	Ensemble e(0);
	//e.Afficher();
} //----- fin de testConctructeurDefaut2

static void testConctructeurDefaut3()
{
	Ensemble e(4);
	//e.Afficher();
	
} //----- fin de testConctructeurDefaut3

static void testConctructeurDefaut()
{
	testConctructeurDefaut1();
	//testConctructeurDefaut2();
	//testConctructeurDefaut3();
	
} //----- fin de testConctructeurDefaut



int main ()
{
	testConctructeurDefaut();
	cout << "BJR" << endl;
	return 0;
} //----- fin de main


