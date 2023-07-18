class LRUCache(val capacity: Int) {
    val cache = mutableMapOf<Int, Int>()

    fun get(key: Int): Int {
        val value = cache[key] ?: return -1
        cache.remove(key)
        cache[key] = value
        return value
    }

    fun put(key: Int, value: Int) {
        if (cache.containsKey(key)) {
            cache.remove(key)
        }
        cache[key] = value
        if(cache.size > capacity) {
            cache.remove(cache.keys.first())
        }
    }
}
