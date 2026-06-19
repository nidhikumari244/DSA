class SnapshotArray {
    // Each index holds a list of [snap_id, value] pairs
    private List<int[]>[] history;
    private int snapId;

    public SnapshotArray(int length) {
        history = new List[length];
        for (int i = 0; i < length; i++) {
            history[i] = new ArrayList<>();
            history[i].add(new int[]{0, 0}); // initial value = 0 at snap 0
        }
        snapId = 0;
    }

    public void set(int index, int val) {
        List<int[]> h = history[index];
        // If last entry is already for current snap_id, just update it
        if (h.get(h.size() - 1)[0] == snapId)
            h.get(h.size() - 1)[1] = val;
        else
            h.add(new int[]{snapId, val});
    }

    public int snap() {
        return snapId++;
    }

    public int get(int index, int snap_id) {
        List<int[]> h = history[index];
        // Binary search for the largest snap_id <= requested snap_id
        int lo = 0, hi = h.size() - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo + 1) / 2;
            if (h.get(mid)[0] <= snap_id) lo = mid;
            else hi = mid - 1;
        }
        return h.get(lo)[1];
    }
}
