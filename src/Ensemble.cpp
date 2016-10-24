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

// type ${file_base}::M�thode ( liste des param�tres )
// Algorithme :
//
//{
//} //----- Fin de M�thode

void Ensemble::Afficher()
// Algorithme :
{
	cout<<cardAct<<"\r\n";
	cout<<cardMax<<"\r\n";
	cout<<'{';
	for(unsigned int i = 0;i<cardAct;i++){
		cout<<tableau[i];
		if(i!=cardAct-1){
			cout<<',';
		}
	}
	cout<<'}'<<"\r\n";
}//----- Fin de M�thode

//TU03
//TU04

crduAjouter Ensemble::Ajouter(int aAjouter)
{
	for(int i = 0; i < cardAct; i++){
		if(tableau[i] == aAjouter){
			return DEJA_PRESENT;
		}
	}

	if(cardMax == cardAct){
		return PLEIN;
	}else if(cardMax > cardAct){
		tableau[cardAct] = aAjouter;
		cardAct = cardAct +1;
		return AJOUTE;
	}
}

unsigned int Ensemble::Ajuster(int delta)
{
	if(delta < 0){
		int nbADelete =  cardAct - cardMax;
		if(delta < nbADelete){
			delta = nbADelete;
		}
	}

	int* temp =  new int [cardMax + delta];
	for(int i = 0; i < cardAct; i++){
		temp[i] = tableau[i];
	}
	delete []tableau;
	tableau = temp;

	cardMax = cardMax + delta;

	return cardMax;
}

bool Ensemble::Retirer (int element)
{
	for(int i = 0; i < cardAct; i++){
		if(tableau[i] == element){
			shift(i+1,-1);
			cardAct--;
			Ajuster(-cardMax);
			return true;
		}
	}
	Ajuster(-cardMax);
	return false;
}




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

Ensemble::Ensemble(int t[],unsigned int nbtableau)
	:cardMax(nbtableau),cardAct(nbtableau)
// Algorithme :z
//
{
	#ifdef MAP
		cout << "Appel au constructeur de <Ensemble>" << endl;
	#endif
	tableau=new int[cardMax];
	for(unsigned int i = 0;i<cardAct;i++){
		tableau[i]=t[i];
	}
	
	quicksort(0,cardAct);
	int old=tableau[0];
	for(unsigned int i = 1;i<cardAct;i++){
		int actual=tableau[i];
		if(old==actual){
			shift(i,-1);
			cardAct--;
			i--;
		}else if(old<actual){
			old=actual;
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

void Ensemble::quicksort(int debut,int fin)
{
	if(debut<fin){
		int pos=partition(debut,fin);
		quicksort(debut,pos);
		quicksort(pos+1,fin);
	}
}
int Ensemble::partition(int debut,int fin)
{
	int swap=0;
	int pivotIndex=debut;
	for(int i = debut+1;i<fin;i++)
	{
		if(tableau[i]<=tableau[debut]){
			pivotIndex++;
			swap=tableau[pivotIndex];
			tableau[pivotIndex]=tableau[i];
			tableau[i]=swap;
			
		}
	}
	swap=tableau[pivotIndex];
	tableau[pivotIndex]=tableau[debut];
	tableau[debut]=swap;
	return pivotIndex;
}
void Ensemble::shift(unsigned int start, int direction)
{
	for(unsigned int i = start;i<cardAct;i++){
		int temp=tableau[i+direction];
		tableau[i+direction]=tableau[i];
		tableau[i]=temp;
	}
}




//----------------------------------------------------- M�thodes prot�g�es

