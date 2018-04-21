#include<GL/glut.h>
#include<stdlib.h>
#include<math.h>
#include<stdio.h>

void *currentfont;

void drawstring(float x,float y,float z,char *string)  
{
	char *c;
	glRasterPos3f(x,y,z);
 
	for(c=string;*c!='\0';c++)
	{
		glutBitmapCharacter(currentfont,*c);
	}
}


void myReshape(GLsizei w, GLsizei h) 
{

	glMatrixMode(GL_PROJECTION);
   	glLoadIdentity(); 
   	glOrtho(0.0, (GLdouble)w, 0.0, (GLdouble)h, -1.0, 1.0);
   	glMatrixMode(GL_MODELVIEW);
   	glViewport(0,0,w,h);
    glFlush();
   
	glutPostRedisplay();
}



void display(void)							
{	

	glClearColor (1.0, 1.0, 1.0, 1.0); 
    glClear(GL_COLOR_BUFFER_BIT);			
	   
	glColor3f(1, 0.98, 0.80);
		glPointSize(1);
		glLineWidth(1);
		glRectf(0,0,60,570);      		// to draw the TOOL BAR 
    		glRectf(0, 0, 800, 30);                 // to draw footer AREA  
		glRectf(0,570, 800, 600);              // to draw MENU BAR


	glColor3f(0, 0, 0);	
	currentfont=GLUT_BITMAP_HELVETICA_12;
	drawstring(250, 10, 0.0, "@ Sagar Dahatonde(16111) & Sagar Nale (16140)");

	glFlush();
}


int main(int argc, char **argv)  
{
	GLsizei w,h;
	glutInit(&argc,argv);
 	glutInitDisplayMode (GLUT_SINGLE| GLUT_RGB);
    
	glutInitWindowSize(800,600);
	glutInitWindowPosition(100, 100);
	glutCreateWindow("SE-I Poject PainBrush");
	
	glutDisplayFunc(display);
	
	glutReshapeFunc(myReshape);
	
	glutMainLoop();
}	
