package com.example.iotsscapp;

import androidx.appcompat.app.AppCompatActivity;
import okhttp3.OkHttpClient;
import okhttp3.logging.HttpLoggingInterceptor;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;
import android.widget.Toast;

import java.util.List;
import java.util.concurrent.TimeUnit;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        getDatabaseResponse();
    }

    private void getDatabaseResponse() {
//        DatabaseAPI databaseAPI = APIClient.getClient().create(DatabaseAPI.class);
        HttpLoggingInterceptor logging = new HttpLoggingInterceptor();
        // set your desired log level
        logging.setLevel(HttpLoggingInterceptor.Level.BODY);

        final OkHttpClient okHttpClient = new OkHttpClient.Builder()
                .readTimeout(30, TimeUnit.SECONDS)
                .connectTimeout(30, TimeUnit.SECONDS)
                .addInterceptor(logging)
                .build();

        final Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://35.197.198.128:2333/")
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        DatabaseAPI databaseAPI = retrofit.create(DatabaseAPI.class);
        Call<List<Sample>> call = databaseAPI.getSamples();

        Log.d("Yo", "here");

        call.enqueue(new Callback<List<Sample>>() {
            @Override
            public void onResponse(Call<List<Sample>> call, Response<List<Sample>> response) {
                Log.d("Get", "on response");
                if (response.isSuccessful()) {
                    List<Sample> sampleList = response.body();
                    Sample latestSample = sampleList.get(sampleList.size() - 1);
                    int classification = latestSample.getClassification();

                    TextView textView = findViewById(R.id.classification);
                    if (classification == 0){
                        textView.setText("You are Walking");
                    }
                    else{
                        textView.setText("You are Running");
                    }
                } else {
                    Log.d("Get", "response not successful!");
                    return;
                }
            }

            @Override
            public void onFailure(Call<List<Sample>> call, Throwable t) {
                Log.d("Get", "on failure");
            }

        });

    }
}
