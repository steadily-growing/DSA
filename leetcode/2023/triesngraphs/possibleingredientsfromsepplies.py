class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        output = []

        for i in range(len(recipes)):
            graph[recipes[i]] = ingredients[i]

        cycle = set()
        def create(recipe):
            if recipe in cycle:
                return False

            if recipe not in graph and recipe not in supplies:
                return False
            
            cycle.add(recipe)

            for r in graph[recipe]:
                if not create(r):
                    return False
            
            cycle.remove(recipe)
                
            return True


        for recipe in recipes:
                if create(recipe):
                    output.append(recipe)
        return output