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

// type ${file_base}::Méthode ( liste des paramètres )
// Algorithme :
//
//{
//} //----- Fin de Méthode

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

bool Ensemble::EstEgal(const Ensemble & unEnsemble) const
{
	if(cardAct==unEnsemble.cardAct){
		for(unsigned int i=0; i<cardAct; i++){
			if(tableau[i]!=unEnsemble.tableau[i]){
				return false;
			}
		}
		return true;
	}
	return false;
}


crduEstInclus Ensemble::EstInclus ( const Ensemble & unEnsemble ) const
{
	if(EstEgal(unEnsemble)){
		return INCLUSION_STRICTE;
	}else{
		if(unEnsemble.cardAct < cardAct){
			return NON_INCLUSION;
		}else{
			for(unsigned int i=0; i<cardAct; i++){
				if(!(unEnsemble.appartenanceEntier(tableau[i]))){
					return NON_INCLUSION;
				}
			}
			return INCLUSION_LARGE;
		}
	}
}

crduAjouter Ensemble::Ajouter(int aAjouter)
{
	for(unsigned int i = 0; i < cardAct; i++){
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
	for(unsigned int i = 0; i < cardAct; i++){
		temp[i] = tableau[i];
	}
	delete []tableau;
	tableau = temp;

	cardMax = cardMax + delta;

	return cardMax;
}

bool Ensemble::Retirer (int element)
{
	for(unsigned int i = 0; i < cardAct; i++){
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

unsigned int Ensemble::Retirer ( const Ensemble & unEnsemble ){

	int tempCardMax = cardMax;
	int tempCardAct = unEnsemble.cardAct;
	unsigned int compteur = 0;
	int* temp =  new int [ unEnsemble.cardMax];
	for(int i = 0; i < tempCardAct; i++){
		temp[i] = unEnsemble.tableau[i];
	}
	for(int i = 0; i <tempCardAct; i++){
		if(Retirer(temp[i])){
			compteur++;
		}
	}

	Ajuster(tempCardMax-cardMax);
	return compteur;

}
int Ensemble::Reunir ( const Ensemble & unEnsemble ){
	bool reajustement=false;
	int tempCardMax = cardMax;
	int tempCardAct = unEnsemble.cardAct;
	int compteur = 0;
	int* temp =  new int [ unEnsemble.cardMax];
	for(int i = 0; i < tempCardAct; i++){
		temp[i] = unEnsemble.tableau[i];
	}
	for(int i = 0; i <tempCardAct; i++){
		crduAjouter resultat=Ajouter(temp[i]);
		if(resultat==AJOUT){
			compteur++;
		}else if(resultat==PLEIN){
			Ajuster(1);
			reajustement=true;
			i--;
		}
	}

	if(reajustement){
		compteur=-compteur;
	}
	return compteur;

}
unsigned int Ensemble::Intersection ( const Ensemble & unEnsemble ){

	int tempCardAct = unEnsemble.cardAct;
	unsigned int compteur = 0;
	int* temp =  new int [ unEnsemble.cardMax];
	for(int i = 0; i < tempCardAct; i++){
		temp[i] = unEnsemble.tableau[i];
	}
	for(int i = 0;i<CardAct;i++){
		bool dansLesDeux=false;
		for(int j = 0; j <tempCardAct; j++){
			if(tableau[i]==temp[i]){
				dansLesDeux=true;	
			}
		}
		if(!dansLesDeux){
			Retirer(tableau[i]);
			compteur++;
		}
	}

	Ajuster(-cardMax);
	return compteur;

}
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

Ensemble::Ensemble(int t[],unsigned int nbtableau)
	:cardMax(nbtableau),cardAct(nbtableau)
// Algorithme :
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
bool Ensemble::appartenanceEntier(int entier) const
{
	bool appartient=false;
	for(int i=0; i<cardAct; i++){
		if(tableau[i]==entier){
			appartient=true;
		}
	}
	return appartient;
}



//----------------------------------------------------- Méthodes protégées

