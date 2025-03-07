while (1) {
    // max jump -- we can jump less
    // greedily pick the furthest position
    int temp = p;
    p += nums[p];
    if (p >= l) return true; // out of bounds ( can reach last index)
    // if (nums[p] == 0) return false;
    if (nums[p] == 0) {
        for (int i = nums[temp]-1; i > 0; i--) {
            cout << "i: " <<  i << endl;
            cout << nums[temp+i] << endl;
            if (nums[temp+i] != 0) {
                p = i; cout << "yur " << endl;
                break;
            }
            cout << "PICKEdddd" << p << endl;
        }
        cout << "end " << endl;
        // check if there's a loop 
        if (nums[p] == 0) return false;
    }
    cout << "p: " << p << endl;
    if (nums[p] == 0) return false;
}