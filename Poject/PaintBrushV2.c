#include<GL/glut.h>
#include<stdlib.h>
#include<math.h>
#include<stdio.h>


void *currentfont;
int i,j,k;


void drawstring(float x,float y,float z,char *string) // to display text 
{
	char *c;
	glRasterPos3f(x,y,z);
 
	for(c=string;*c!='\0';c++)
	{
		glutBitmapCharacter(currentfont,*c);
	}
}


void setFont(void *font)
{
	currentfont=font;
}


void palette(float x1, float y1, float x2, float y2, float x3, float y3, float x4, float y4) // to draw the COLOR PALETTE 
{
	glBegin(GL_QUADS);
		glVertex2f(x1, y1);
		glVertex2f(x2, y2);
		glVertex2f(x3, y3);
		glVertex2f(x4, y4);
	glEnd();
}


void myReshape(GLsizei w, GLsizei h) // RESHAPE FUNCTION 
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
	   
   glColor3f(1.0, 0.98, 0.80);
	glPointSize(1);
	glLineWidth(1);
	glRectf(0,0,60,570);                     // to draw the TOOL BAR 
    glRectf(0, 0, 800, 30);                 // to draw Footer AREA  
	glRectf(0,570, 800, 600);              // to draw MENU BAR

	setFont(GLUT_BITMAP_HELVETICA_12);
	glColor3f(0, 0, 0);	
	drawstring(250, 10, 0.0, "@ Sagar Dahatonde(16111) & Sagar Nale (16140)");


 /* Drow Tool Box Panel */
	glColor3f(0, 0, 0);
 
	glBegin(GL_LINE_LOOP);                               
		glVertex2f(2,569);
		glVertex2f(58,569);
		glVertex2f(58,480);
		glVertex2f(2, 480);
	glEnd();

	glBegin(GL_LINES);
		glVertex2f(30, 569);
		glVertex2f(30, 480);

		glVertex2f(2, 540);
		glVertex2f(58, 540);

		glVertex2f(2, 510);
		glVertex2f(58, 510);
		
		glVertex2f(2, 480);
		glVertex2f(58, 480);
	glEnd();


    /* draw COLOR PALETTE */ 
	 
	glColor3f(0, 0, 0);
	palette(2.0, 470,2.0,450,22,450,22,470);
	
	glColor3f(1, 1, 1);
	palette(26,470,26,450,46,450,46,470);

	glColor3f(0, 0, 1);
	palette(2,446,2,426,22,426,22,446);

	glColor3f(1, 0, 1);
	palette(26,446,26,426,46,426,46,446);

	glColor3f(1, 1, 0);
	palette(2,424,2,404,22,404,22,424);

	glColor3f(1, 0, 0);
	palette(26,424,26,404,46,404,46,424);

	glColor3f(0, 1, 0);
	palette(2,402,2,382,22,382,22,402);


	glColor3f(0, 1, 1);
	palette(26,402,26,382,46,382,46,402);
	



    /*Drow Sheps of Tool Bar  */

    glColor3f(0, 0, 0);
    
    glBegin(GL_LINES);                             // for line 
		glVertex2f(40, 564);      
		glVertex2f(50, 546);
	glEnd();

	
	glBegin(GL_LINE_LOOP);                        // For Trangle
		glVertex2f(15, 534);
		glVertex2f(05, 516);
		glVertex2f(25, 516);
	glEnd();
                                               
	glBegin(GL_LINE_LOOP);                         // For Rectangle 
		glVertex2f(35, 534);
		glVertex2f(54, 534);
		glVertex2f(54, 516);
		glVertex2f(35, 516);
	glEnd();
    

    glColor3f(1, 1, 1);                              // For Eraser
	glBegin(GL_QUADS);
		glVertex2f(10, 549);
		glVertex2f(10, 564);
		glVertex2f(22, 564);
		glVertex2f(22, 549);	
	glEnd();


    
    glColor3f(0.4, 0.1, 0.1);
	glBegin(GL_QUADS);                                 // for paint pain
		glVertex2f(35, 495);
		glVertex2f(50, 495); 
		glVertex2f(50, 498);
		glVertex2f(35, 498);
	glEnd();

    glColor3f(0, 0, 0);
	
	for(i=0;i<40;i++)					             // for point brush
	    {
             j=rand()%15;
			 k=rand()%15;
			 glBegin(GL_POINTS);
			 glVertex2f(6+j,504-k);
			 glEnd();
         }
	
glFlush();
}

int main(int argc, char **argv)  
{

	glutInit(&argc,argv);
 	glutInitDisplayMode (GLUT_SINGLE| GLUT_RGB);
    
	glutInitWindowSize(800,600);
	glutInitWindowPosition(100, 100);
	glutCreateWindow("PainBrush");
		
	glutReshapeFunc(myReshape);

	glutDisplayFunc(display);
  
	glutMainLoop();
}	