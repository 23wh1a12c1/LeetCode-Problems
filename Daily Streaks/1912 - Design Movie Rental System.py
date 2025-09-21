#####    PYTHON3

from typing import List, Tuple
from collections import defaultdict
import bisect

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        # price dictionary: (shop, movie) -> price
        self.price = {}
        # unrented: movie -> sorted list of (price, shop)
        self.unrented = defaultdict(list)
        # rented: sorted list of (price, shop, movie)
        self.rented = []

        # For quick lookups and removals from unrented and rented, use dicts of sets too
        self.unrented_set = defaultdict(set)
        self.rented_set = set()

        for shop, movie, p in entries:
            self.price[(shop, movie)] = p
            # insert in sorted order for unrented[movie]
            bisect.insort(self.unrented[movie], (p, shop))
            self.unrented_set[movie].add((p, shop))

    def search(self, movie: int) -> List[int]:
        # Return up to 5 shops with unrented copies of the movie sorted by price then shop
        ans = []
        for price_shop in self.unrented[movie][:5]:
            ans.append(price_shop[1])
        return ans

    def rent(self, shop: int, movie: int) -> None:
        p = self.price[(shop, movie)]
        # Remove from unrented
        if (p, shop) in self.unrented_set[movie]:
            self.unrented_set[movie].remove((p, shop))
            idx = bisect.bisect_left(self.unrented[movie], (p, shop))
            if idx < len(self.unrented[movie]) and self.unrented[movie][idx] == (p, shop):
                self.unrented[movie].pop(idx)

        # Add to rented
        key = (p, shop, movie)
        # Insert into rented in sorted order by price, shop, movie
        idx = bisect.bisect_left(self.rented, key)
        self.rented.insert(idx, key)
        self.rented_set.add(key)

    def drop(self, shop: int, movie: int) -> None:
        p = self.price[(shop, movie)]
        key = (p, shop, movie)
        if key in self.rented_set:
            self.rented_set.remove(key)
            idx = bisect.bisect_left(self.rented, key)
            if idx < len(self.rented) and self.rented[idx] == key:
                self.rented.pop(idx)

        # Add back to unrented
        if (p, shop) not in self.unrented_set[movie]:
            bisect.insort(self.unrented[movie], (p, shop))
            self.unrented_set[movie].add((p, shop))

    def report(self) -> List[List[int]]:
        # Return up to 5 rented movies sorted by price, shop, movie
        ans = []
        for i in range(min(5, len(self.rented))):
            _, shop, movie = self.rented[i]
            ans.append([shop, movie])
        return ans




#####   JAVA


import java.util.*;

public class MovieRentingSystem {
    // Map of (shop, movie) -> price
    private Map<String, Integer> price;
    // Map movie -> TreeSet of (price, shop), sorted by price then shop
    private Map<Integer, TreeSet<ShopPrice>> unrented;
    // TreeSet of rented (price, shop, movie) sorted by price, shop, movie
    private TreeSet<RentedEntry> rented;

    public MovieRentingSystem(int n, int[][] entries) {
        price = new HashMap<>();
        unrented = new HashMap<>();
        rented = new TreeSet<>();

        for (int[] e : entries) {
            int shop = e[0], movie = e[1], p = e[2];
            price.put(shop + "," + movie, p);

            unrented.computeIfAbsent(movie, k -> new TreeSet<>())
                    .add(new ShopPrice(p, shop));
        }
    }

    public List<Integer> search(int movie) {
        List<Integer> ans = new ArrayList<>();
        TreeSet<ShopPrice> set = unrented.getOrDefault(movie, new TreeSet<>());
        Iterator<ShopPrice> it = set.iterator();
        int count = 0;
        while (it.hasNext() && count < 5) {
            ans.add(it.next().shop);
            count++;
        }
        return ans;
    }

    public void rent(int shop, int movie) {
        int p = price.get(shop + "," + movie);
        TreeSet<ShopPrice> set = unrented.get(movie);
        if (set != null) {
            set.remove(new ShopPrice(p, shop));
        }
        rented.add(new RentedEntry(p, shop, movie));
    }

    public void drop(int shop, int movie) {
        int p = price.get(shop + "," + movie);
        rented.remove(new RentedEntry(p, shop, movie));
        unrented.computeIfAbsent(movie, k -> new TreeSet<>())
                .add(new ShopPrice(p, shop));
    }

    public List<List<Integer>> report() {
        List<List<Integer>> ans = new ArrayList<>();
        Iterator<RentedEntry> it = rented.iterator();
        int count = 0;
        while (it.hasNext() && count < 5) {
            RentedEntry re = it.next();
            ans.add(Arrays.asList(re.shop, re.movie));
            count++;
        }
        return ans;
    }

    // Helper class to store shop and price, sorted by price then shop
    private static class ShopPrice implements Comparable<ShopPrice> {
        int price, shop;

        ShopPrice(int price, int shop) {
            this.price = price;
            this.shop = shop;
        }

        public int compareTo(ShopPrice other) {
            if (this.price != other.price) {
                return this.price - other.price;
            }
            return this.shop - other.shop;
        }

        @Override
        public boolean equals(Object o) {
            if (!(o instanceof ShopPrice)) return false;
            ShopPrice sp = (ShopPrice) o;
            return this.price == sp.price && this.shop == sp.shop;
        }

        @Override
        public int hashCode() {
            return Objects.hash(price, shop);
        }
    }

    // Helper class to store rented entries sorted by price, shop, movie
    private static class RentedEntry implements Comparable<RentedEntry> {
        int price, shop, movie;

        RentedEntry(int price, int shop, int movie) {
            this.price = price;
            this.shop = shop;
            this.movie = movie;
        }

        public int compareTo(RentedEntry other) {
            if (this.price != other.price) {
                return this.price - other.price;
            }
            if (this.shop != other.shop) {
                return this.shop - other.shop;
            }
            return this.movie - other.movie;
        }

        @Override
        public boolean equals(Object o) {
            if (!(o instanceof RentedEntry)) return false;
            RentedEntry re = (RentedEntry) o;
            return this.price == re.price && this.shop == re.shop && this.movie == re.movie;
        }

        @Override
        public int hashCode() {
            return Objects.hash(price, shop, movie);
        }
    }
}


#####    C++



class MovieRentingSystem {
    map<pair<int, int>, int> price; // {shop, movie} -> price
    unordered_map<int, set<pair<int, int>>> unrented; // movie -> set of {price, shop}
    set<tuple<int, int, int>> rented; // set of {price, shop, movie}
public:
    MovieRentingSystem(int n, vector<vector<int>>& entries) {
        for (auto &e : entries) {// shop, movie, price
            int shop = e[0], movie = e[1], p = e[2];
            price[{shop, movie}] = p; 
            unrented[movie].emplace(p, shop);
        }
    }
    vector<int> search(int movie) {
        auto &s = unrented[movie];
        vector<int> ans;
        int i = 0;
        for (auto it = s.begin(); i < 5 && it != s.end(); ++it, ++i) {
            ans.push_back(it->second);
        }
        return ans;
    }
    void rent(int shop, int movie) {
        int p = price[{shop, movie}];
        unrented[movie].erase({p, shop});
        rented.emplace(p, shop, movie);
    }
    void drop(int shop, int movie) {
        int p = price[{shop, movie}];
        rented.erase({p, shop, movie});
        unrented[movie].emplace(p, shop);
    }
    vector<vector<int>> report() {// shop, movie
        vector<vector<int>> ans;
        int i = 0;
        for (auto it = rented.begin(); it != rented.end() && i < 5; ++i, ++it) {
            auto [p, s, m] = *it;
            ans.push_back({s, m});
        }
        return ans;
    }
};
