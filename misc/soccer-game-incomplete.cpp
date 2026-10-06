/*
   https://contest.usc.edu/pmwiki.php/Main/Spring26?action=download&upname=spring2026.pdf
   problem a
*/













#include <bits/stdc++.h>
using namespace std;




bool check_player(set<string>& t1, set<string>& t2, string name) {
    return t1.count(name) || t2.count(name);
}


bool check_same_team(set<string>& t1, set<string>& t2, string name, string name2) {
    if (t1.count(name) != 0) {
        if (t1.count(name2) == 0) return false;
    } else if (t2.count(name) != 0) {
        if (t2.count(name2) == 0) return false;
    }
    return true;
}


int main() {
    int k;
    cin >> k;




    while (k--) {
        int r, n, v; // num plrs roster, num on field each team, number of game evnts
        cin >> r >> n >> v;

        // first n are on the field at start
        set<string> t1;
        set<string> t2;

        // playing rn
        set<string> curr1;
        set<string> curr2;


        // t 1
        string name;
        int t = 0;
        for (int i =0; i <  r; i++) {
            cin >> name;
            if (t< n) {
                curr1.insert(name);
                t++;
            }
            
            t1.insert(name);
        }
        t = 0;
        for (int i =0; i <  r; i++) {
            cin >> name;
            // put n onto start  
            if (t< n) {
                curr2.insert(name);
                t++;
            }
            t2.insert(name);
        }

        string event;
        string name2;


        map<string, int> yellows1;
        map<string, int> yellows2;

        int score1, score2;
        for (int i = 0; i < v; i++) {
            // v events
            cin >> event;
            if (event == "GOAL") {
                cin >> name;
                if (t1.count(name) != 0) score1++;
                else if (t2.count(name) != 0 )score2++;

            }
            else if (event == "OWNGOAL") {
                cin >> name;
                if (t1.count(name) != 0) score2++;
                else if (t2.count(name) != 0) score1++;
            }
            else if (event == "YELLOW") {
                cin >> name;
                if (t1.count(name) != 0) {
                    yellows1[name]++;
                } else if (t2.count(name) != 0) yellows2[name]++;

            }
            else if (event == "RED") {
                cin >> name;
                if (t1.count(name) != 0) {
                    yellows1[name] = 2;
                } else if (t2.count(name) != 0) yellows2[name] = 2;
            }
            else if (event == "SUB") {
                cin >> name >> name2;
                if (t1.count(name) != 0) {
                    curr1.erase(name);
                    curr1.insert(name2);
                } else if (t2.count(name) != 0) {
                    curr2.erase(name);
                    curr2.insert(name2);
                }

            }



        }
        


        





    }







    return 0;
}




