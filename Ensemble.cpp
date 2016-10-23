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
		cout<<tableau[i];
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

Ensemble::Ensemble(int t[],unsigned int nbElements)
	:cardMax(nbElements),cardAct(t.length)
// Algorithme : 
//1- copie de tout les el de t
//2-tri avec le quicksort
//3- suppression des doublons: (si egalité avec la mémoire, on echange l'el avec la fin (en faisant un shift pour garder l'ordre),
// puis on decremente la taille de la collection
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
		
		if(old==tableau[i]){
			shift(i,-1);
			cardAct--;
		}else if(old<tableau[i]){
			old=tableau[i];
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
//Algorithme: fct recursive qui coupe le tableau en deux autour d'un pivot (cf quicksort cours algo)
{
	if(debut<fin){
		int pos=partition(debut,fin);
		quicksort(debut,pos-1);
		quicksort(pos+1,fin);
	}
}
int Ensemble::partition(int debut,int fin)
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
//----------------------------------------------------- Méthodes protégées

