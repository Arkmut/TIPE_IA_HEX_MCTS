/*************************************************************************
                           ${file_base}  -  description
                             -------------------
    d�but                : ${date}
    copyright            : (C) ${year} par ${user}
*************************************************************************/

//---------- R�alisation de la classe Ensemble -------

//---------------------------------------------------------------- INCLUDE

//-------------------------------------------------------- Include syst�me
using namespace std;
#include <iostream>

//------------------------------------------------------ Include personnel
#include "Ensemble.h"

//------------------------------------------------------------- Constantes

//----------------------------------------------------------------- PUBLIC

//----------------------------------------------------- M�thodes publiques
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
}//----- Fin de M�thode
// type ${file_base}::M�thode ( liste des param�tres )
// Algorithme :
//
//{
//} //----- Fin de M�thode


//------------------------------------------------- Surcharge d'op�rateurs

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

//----------------------------------------------------- M�thodes prot�g�es

