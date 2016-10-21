/*************************************************************************
                           ${file_base}  -  description
                             -------------------
    début                : ${date}
    copyright            : (C) ${year} par ${user}
*************************************************************************/

//---------- Réalisation de la classe Ensemble -------

//---------------------------------------------------------------- INCLUDE

//-------------------------------------------------------- Include système
using namespace std;
#include <iostream>

//------------------------------------------------------ Include personnel
#include "Ensemble.h"

//------------------------------------------------------------- Constantes

//----------------------------------------------------------------- PUBLIC

//----------------------------------------------------- Méthodes publiques
void Ensemble::Afficher()
// Algorithme :
{
	cout<<cardAct<<"\r\n";
	cout<<cardMax<<"\r\n";
	cout<<'{';
	for(unsigned int i = 0;i<cardAct;i++){
		cout<<(*tableau)[i];
		if(i!=cardAct-1){
			cout<<',';
		}
	}
	cout<<'}'<<"\r\n";
}//----- Fin de Méthode
// type ${file_base}::Méthode ( liste des paramètres )
// Algorithme :
//
//{
//} //----- Fin de Méthode


//------------------------------------------------- Surcharge d'opérateurs

//-------------------------------------------- Constructeurs - destructeur


Ensemble::Ensemble (unsigned int cMax)
	:cardMax(cMax),cardAct(0)
// Algorithme :
//
{
	#ifdef MAP
		cout << "Appel au constructeur de <Ensemble>" << endl;
	#endif
	tableau=new int[cardMax];



} //----- Fin de Ensemble


Ensemble::~Ensemble( )
// Algorithme :
//
{
	#ifdef MAP
		cout << "Appel au destructeur de <Ensemble>" << endl;
	#endif
	delete [] tableau;
} //----- Fin de ~Ensemble


//------------------------------------------------------------------ PRIVE

//----------------------------------------------------- Méthodes protégées

