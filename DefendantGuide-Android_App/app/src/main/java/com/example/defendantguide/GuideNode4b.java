package com.example.defendantguide;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class GuideNode4b extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_guide_node4b);
    }
    public void onHomePressed(View v){
        setResult(RESULT_OK);
        finish();
    }
    public void onBackPressed() {
        super.onBackPressed();
        overridePendingTransition(R.anim.left_slide_in, R.anim.right_slide_out);
    }
    public void pressBackButton(View v){
        onBackPressed();
    }
}
