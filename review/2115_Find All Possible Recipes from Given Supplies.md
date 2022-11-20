# [2115\. Find All Possible Recipes from Given Supplies](https://leetcode.cn/problems/find-all-possible-recipes-from-given-supplies/)

## Description

Difficulty: **中等**  

Related Topics: [Graph](https://leetcode.cn/tag/graph/), [Topological Sort](https://leetcode.cn/tag/topological-sort/), [Array](https://leetcode.cn/tag/array/), [Hash Table](https://leetcode.cn/tag/hash-table/), [String](https://leetcode.cn/tag/string/)


You have information about `n` different recipes. You are given a string array `recipes` and a 2D string array `ingredients`. The i<sup>th</sup> recipe has the name `recipes[i]`, and you can **create** it if you have **all** the needed ingredients from `ingredients[i]`. Ingredients to a recipe may need to be created from **other** recipes, i.e., `ingredients[i]` may contain a string that is in `recipes`.

You are also given a string array `supplies` containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return _a list of all the recipes that you can create._ You may return the answer in **any order**.

Note that two recipes may contain each other in their ingredients.

**Example 1:**

```
Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
```

**Example 2:**

```
Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
```

**Example 3:**

```
Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".
```

**Constraints:**

*   `n == recipes.length == ingredients.length`
*   `1 <= n <= 100`
*   `1 <= ingredients[i].length, supplies.length <= 100`
*   `1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10`
*   `recipes[i], ingredients[i][j]`, and `supplies[k]` consist only of lowercase English letters.
*   All the values of `recipes` and `supplies` combined are unique.
*   Each `ingredients[i]` does not contain any duplicate values.


## Solution

Language: java

```java
class Solution {
    public List<String> findAllRecipes(String[] recipes, List<List<String>> ingredients, String[] supplies) {
        // build graph
        Map<String, List<String>> graph = new HashMap<>();
        // indegree 
        Map<String, Integer> indegree = new HashMap<>();
        for (int i = 0; i < ingredients.size(); i++) {
            List<String> ingredient = ingredients.get(i);
            String recipe = recipes[i];
            for (int j = 0; j < ingredient.size(); j++) {
                String tmpIngredient = ingredient.get(j);
                List<String> tmp = graph.getOrDefault(tmpIngredient, new ArrayList<>());
                tmp.add(recipe);
                graph.put(tmpIngredient, tmp);
                indegree.put(recipe, indegree.getOrDefault(recipe, 0) + 1);
            }
        }
         
        // System.out.println(indegree.get("bread"));
        ArrayDeque<String> queue = new ArrayDeque<>();
        for (String s : supplies) {
            queue.offerLast(s);
            // System.out.println(s);
        }
        System.out.println(queue.size());
        List<String> res = new ArrayList<>();
        while (!queue.isEmpty()) {
            String s = queue.pollFirst();
            if (graph.containsKey(s)) {
                List<String> edges = graph.get(s); // "bread"
                // for (String xx : edges) {
                //     System.out.println(xx);
                // }
                for (String e : edges) {
                    // System.out.println("start");
```
