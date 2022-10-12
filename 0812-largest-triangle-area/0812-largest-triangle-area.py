class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        def area(p1,p2,p3):
            x1,y1=p1
            x2,y2=p2
            x3,y3=p3
            return 0.5*(x1*y2+x2*y3+x3*y1-x3*y2-x2*y1-x1*y3)

        def boundary(points):
            points=sorted(points,key=lambda p: (p[0],p[1]))
            def cross(o,a,b): return (o[0]-a[0])*(o[1]-b[1])-(o[1]-a[1])*(o[0]-b[0])
            lower=[]
            for p in points:
                while len(lower)>=2 and cross(lower[-2],lower[-1],p)<0: lower.pop()
                lower.append(tuple(p))
            upper=[]
            for p in reversed(points):
                while len(upper)>=2 and cross(upper[-2],upper[-1],p)<0: upper.pop()
                upper.append(tuple(p))
            return list(set(lower[:-1]+upper[:-1]))

        res=0
        bound=boundary(points)
        for p1,p2,p3 in itertools.permutations(bound,3):
            tmp=area(p1,p2,p3)
            if tmp>res: res=tmp
        return res
