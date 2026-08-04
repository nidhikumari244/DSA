class LUPrefix {

    private boolean[] uploaded;
    private int longest;

    public LUPrefix(int n) {
        uploaded = new boolean[n + 2];
        longest = 0;
    }

    public void upload(int video) {
        uploaded[video] = true;

        while (uploaded[longest + 1]) {
            longest++;
        }
    }

    public int longest() {
        return longest;
    }
}

/**
 * Your LUPrefix object will be instantiated and called as such:
 * LUPrefix obj = new LUPrefix(n);
 * obj.upload(video);
 * int param_2 = obj.longest();
 */
