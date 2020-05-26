# Solving poisson equation in 2D
We want to solve the 2D poisson equation using Python

poisson equation : ∂2u/∂x2 + ∂2u/∂y2 = b

Spatial domain : X ∈(0,2) Y ∈(0,2)


The source term of poisson equation was assigned by "b" which is:
 								   #b= 200 at   x(0.4,0.6), y(0.4,0.6)
								   #b= -200 at  x(0.4,0.6), y(0.4,0.6)
								   
								   
								   #b= 0    at  everywhere else
								   
Boundery Conditions : u= 0 for x=0, 2 
		       u= 0 for y=0, 2
