using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;


namespace Mizuyari_app
{
    public partial class watersprrinkler : Form
    {
        private int trackBar1_value_before = 0; // �g���b�N�o�[�̑O��l
        public watersprrinkler()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void progressBar1_Click(object sender, EventArgs e)
        {

        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
        
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void exit_button_Click(object sender, EventArgs e)
        {
            MessageBox.Show("�A�v���P�[�V�������I������܂���");
            this.Close();
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            {
                int diff = trackBar1.Value - trackBar1_value_before; // �O��Ƃ̍������v�Z

                textBox2.Text = (int.Parse(textBox2.Text) + diff).ToString(); // �e�L�X�g�{�b�N�X�ɍ����𔽉f

                trackBar1_value_before = trackBar1.Value; // �O��̒l�����ݒl�ōX�V
            }

        }
        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            MessageBox.Show( "�����̎��x��"+ hum_textBox.Text +"%�ł�" );
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void trackBar2_Scroll(object sender, EventArgs e)
        {
           
         
        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {

        }
    }
}