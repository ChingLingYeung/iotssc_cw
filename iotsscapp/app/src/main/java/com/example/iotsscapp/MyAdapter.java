package com.example.iotsscapp;

import android.content.Context;
import android.text.Layout;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import java.util.ArrayList;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class MyAdapter extends RecyclerView.Adapter<MyAdapter.MyViewHolder> {

    ArrayList<String> ts, cls;
    Context context;

    public MyAdapter(Context context, ArrayList<String> ts, ArrayList<String> cls){
        this.context = context;
        this.ts = ts;
        this.cls = cls;
    }

    @NonNull
    @Override
    public MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(context);
        View view = inflater.inflate(R.layout.recycler_row, parent, false);
        return new MyViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull MyViewHolder holder, int position) {
        holder.tsText.setText(ts.get(position));
        holder.clsText.setText(cls.get(position));

    }

    @Override
    public int getItemCount() {
        return ts.size();
    }

    public class MyViewHolder extends RecyclerView.ViewHolder{

        TextView tsText, clsText;

        public MyViewHolder(@NonNull View itemView) {
            super(itemView);
            tsText = itemView.findViewById(R.id.timestampText);
            clsText = itemView.findViewById(R.id.classificationText);
        }
    }
}
