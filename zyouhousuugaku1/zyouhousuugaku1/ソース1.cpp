#include <stdio.h>



int cnt = 0; //���Z�񐔂��i�[����ϐ�

int fibo(int n) {
	if (n == 0) return 0; //�t�B�{�i�b�`����̒�`
	if (n == 1) return 1;
	if (n >= 2) {
		cnt++;
		return fibo(n - 1) + fibo(n - 2);
	}
}



int main(void) {
	int num;
	printf("�扽���̃t�B�{�i�b�`��Fn�����߂܂����H�F");
	scanf_s("%d",&num);

	printf("��%d���̃t�B�{�i�b�`�����%d�ł��B ", num, fibo(num));
	printf("���Z�񐔂�%d��ł��B ", cnt);
	return(0);
}