class MyHashSet {

    // Boolean array to store whether a key exists
    private boolean[] set;

    public MyHashSet() {

        // Keys range from 0 to 10^6
        set = new boolean[1000001];
    }

    public void add(int key) {

        set[key] = true;
    }

    public void remove(int key) {

        set[key] = false;
    }

    public boolean contains(int key) {

        return set[key];
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */
