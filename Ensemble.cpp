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

Ensemble::Ensemble(int t[],unsigned int nbElements);
	:cardMax(nbElements),cardAct(t.length)
// Algorithme :
//
{
	#ifdef MAP
		cout << "Appel au constructeur de <Ensemble>" << endl;
	#endif
	tableau=new int[cardMax];
	for(int i = 0;i<cardAct;i++){
		tableau[i]=t[i];
	}
	quicksort(0,cardAct);
	for(int i = 1;i<cardAct;i++){
		int old=tableau[i-1];
		if(old==tableau[i]){
			shift(i,-1);
			cardAct--;
		}
	}


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

void quicksort(int debut,int fin)
{
	if(debut<fin){
		int pos=partition(debut,fin);
		quicksort(debut,pos-1);
		quicksort(pos+1,fin);
	}
}
int partition(int debut,int fin)
{
	int swap=tableau[debut];
	tableau[debut]=tableau[fin/2];
	tableau[fin/2]=swap;
	int pivotIndex=debut;
	for(int i = debut+1;i<fin;i++)
	{
		if(tableau[i]<tableau[debut]){
			pivotIndex++;
			swap=tableau[pivotIndex];
			tableau[pivotIndex]=tableau[i];
			tableau[i]=swap;
			
		}
	}
	swap=tableau[pivotIndex];
	tableau[pivotIndex]=tableau[d];
	tableau[d]=swap;
	return pivotIndex;
}
void shift(int start, int direction)
{
	for(int i = start;i<cardAct;i++){
		int temp=tableau[i+direction];
		tableau[i+direction]=tableau[i];
		tableau[i]=temp;
	}
}
//----------------------------------------------------- Méthodes protégées

